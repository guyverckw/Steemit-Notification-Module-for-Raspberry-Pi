from piston.steem import Steem
from piston.account import Account
from RPLCD.i2c import CharLCD

import time
import RPi.GPIO as GPIO
import sys

# initialize Steem
account_name = 'guyverckw'
account = Account(account_name)
steem = Steem()

# initialize LCD
lcd = CharLCD('PCF8574', 0x3f)

# Clear LCD
print('Clear LCD')

# Prepare LED indicator
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

# Set user account, no. of history retrieve everytime, transaction ID buffer array of 10 
first = 9999999999
limit = 5
History = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
History_ID = 1.0
message = ' '

# keep checking transactions
while True:
	try:
		index = 0
		print (History, History_ID)

# Get last 5 history, put ID into buffer array
		for his in account.rawhistory(first, limit):
			if History_ID == his[0]:
				break
			print('History ID: %d10.0' % History_ID)
			print(his[1]['op'])
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
			print (message)
			GPIO.output(11, GPIO.HIGH)
			lcd.clear()
			lcd.write_string(message)
			time.sleep(1)
			GPIO.output(11, GPIO.LOW)

		History_ID = History[0] 
	except KeyboardInterrupt:
		break
	except Exception as e:
		print(e)
		continue
