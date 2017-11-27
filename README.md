# Steemit-Notification-Module-for-Raspberry-Pi
Notification of your Steemit account activity on Raspberry Pi platform

Setup Procedure: (Draft)

​
Notification module setup procedures


1. Install Raspbian

2. Install Python 3.6 (actually done need)


Pre-requisites

Open the terminal (command prompt) and run the following commands. These will install the pre-requisites

i)sudo apt-get install build-essential checkinstall

ii) sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev


Download Python 3.6

Next step is to download from the Python site. Once you’ve downloaded it you will need to extract it (hence line 3)

i) wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz

ii) sudo tar xzf Python-3.6.3.tgz


Compile Python

Next we need to compile. This step will take a while.

i) cd Python-3.6.0

ii) sudo -s

iii) bash configure

iv) make altinstall

v) exit


Set python3.6.3 as default python3

i) rm /usr/bin/python3

ii) ln /usr/local/bin/python3.6 /usr/bin/python3


3) Install LCD library -- RPLCD

Setup


You can install RPLCD directly from PyPI using pip:


i) $ sudo pip3 install RPLCD (for python2 use pip)

If you want to use I2C, you also need smbus:


ii) $ sudo apt-get install python3-smbus (for python2 use python-smbus)


You can also install the library manually without pip. Either just copy the scripts to your working directory and import them, or download the repository and run python setup.py install to install it into your Python package directory.


4) Install Python-steem (piston-steem)


sudo apt-get update

sudo apt-get upgrade


$ git clone https://github.com/xeroc/piston-lib/

$ cd piston-lib

$ python3 setup.py install --user


if get "fatal error: openssl/aes.h : No such file or directory" error, you may need to install Openssl Development package


sudo apt-get install libssl-dev









==========================================


https://discourse.mopidy.com/t/solved-help-to-attach-a-lcd-20x4-i2c-to-a-raspy-a-with-pi-dac/836/12
