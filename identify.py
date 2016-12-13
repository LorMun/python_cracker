#!/usr/bin/python

import sys
import importlib
from crack_md5 import *
from crack_sha1 import *

def choice (default="y"):
	if (default=="y"):
		yes = set(['yes','y', 'ye', ''])
		no = set(['no','n'])
	else:
		yes = set(['yes','y', 'ye'])
		no = set(['no','n', ''])
		
	choice = raw_input().lower()
	if choice in yes:
		return True
	elif choice in no:
		return False
	else:
		print("Please respond with 'yes' or 'no'")

def identifiy (hash):
	print "\n---------------------Parameters ---------------------"
	print 'Hash:', hash
	print "\n---------------------Identifier---------------------"
	found = 0
	if len(hash)==32:
		found = 1
		print "Your hash might be a MD5.\n\n\nDo you wish to crack the hash? (Y/n)"
		if(choice()):
			print "Do you want to use the default wordlist? (Y/n)"
			if(choice()):
				crack_md5 (hash, "wordlist/wordlist.txt")
			else:
				print "Please insert your wordlist:"
				crack_md5 (hash, raw_input())
	
	if len(hash)==40:
		found = 1
		print "Your hash might be a SHA1.\n\n\nDo you wish to crack the hash? (Y/n)"
		if(choice()):
			print "Do you want to use the default wordlist? (Y/n)"
			if(choice()):
				crack_sha1 (hash, "wordlist/wordlist.txt")
			else:
				print "Please insert your wordlist:"
				crack_sha1 (hash, raw_input())
			
	if (not(found)):
		print "Unknown hash"
		