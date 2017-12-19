from piston.steem import Steem
from piston.account import Account
from piston.blog import Blog
from piston.post import Post

from demo_opts import get_device
from luma.core import cmdline
from luma.core.virtual import terminal, viewport
from PIL import ImageFont

import os
import threading
import random
import csv
import urllib.request
import time
import RPi.GPIO as GPIO
import sys

def make_font(name, size):
	font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', name))
	return ImageFont.truetype(font_path, size)


def main():
	# Set user account, no. of history retrieve everytime, transaction ID buffer array of 10 
	account_name = 'guyverckw'
	account = Account(account_name)
	steem = Steem()
	first = 9999999999
	limit = 5
	History = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	History_ID = 1.0
	message = ' '

	# Prepare LED indicator
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)


	# Prepare for OLED display, first prepare the device with built-in parameter for 12832 screen
	device_args = ['-d', 'ssd1306', '--width', '128', '--height', '32']
	parser = cmdline.create_parser(description='luma.examples arguments')
	args = parser.parse_args(device_args)
	device = cmdline.create_device(args)

	# Set font 
	font = make_font('ProggyTiny.ttf', 16)
	term = terminal(device, font)
	term.clear()
	term.animate = False

	# keep checking transactions
	while True:
		index = 0

		# Get last 5 history, put ID into buffer array
		for his in account.rawhistory(first, limit):
			if History_ID == his[0]:
				break
			if his[1]['op'][0] == 'comment':
				message = 'There is a comment from @' + his[1]['op'][1]['author']
			elif his[1]['op'][0] == 'vote':
				if his[1]['op'][1]['author'] == account_name:
					message = 'There is a vote from @' + his[1]['op'][1]['voter'] + ' of ' + str(his[1]['op'][1]['weight']/100) +'%'
			else: 
				History[index] = his[0]
				index += 1
				continue
			History[index] = his[0]
			index += 1
			# print (message)
			GPIO.output(11, GPIO.HIGH)
			term.clear()
			term.println(message)
			time.sleep(1)
			GPIO.output(11, GPIO.LOW)

		History_ID = History[0] 

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	except Exception as e:
		print(e)
