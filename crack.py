#!/usr/bin/python

import time
import sys
import getopt
from crack_md5 import *
from crack_sha1 import *
from identify import *

def get_mode():
	print "test"

def get_input():
	usage = "To identifiy the hash use 'python crack.py -i <hashvalue>'.\nTo crack the hash use 'python crack.py -c <hashvalue> <wordlist-file>'"

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'c:i:m:h', ['crack=', 'identify=', 'mode=', 'help'])
		test = opts
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	flag = 0
	helper = opts
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print usage
		elif opt in ('-i', '--identify'):
			identifiy(sys.argv[2])
		elif (opt in ('-c', '--crack')):
			for blubb in test:
				if blubb in ('-m', '--mode'):
					get_mode()
					sys.exit(0)
		else:
			print usage
			sys.exit(2)

get_input()