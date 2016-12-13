from time import *
import hashlib

def crack_md5(hash, wordlist):
	print "\n---------------------Parameters ---------------------"
	print 'Hash:', hash
	print 'Wordlistpath:', wordlist

	f = open(wordlist, 'r+')

	print "\n---------------------Start cracker---------------------"

	counter = 0

	t1 = clock()
	for line in f:
		counter += 1
		
		if counter%500000 == 0:
			print counter, "Hashes calculated"
		
		calc = hashlib.md5(line).hexdigest()
		
		if hash == calc:    
			print "\n============Result================\n\nYour Password is", line 
			break		
	else:
		print "\nNo Hash found! Maybe try another wordlist."
	t2 = clock()

	dt = t2 - t1
	print "\nHad to try", counter, "Hashes.\nCalculated", dt, "Seconds."