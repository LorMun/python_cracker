#!/usr/bin/python
import os
import inspect
from time import *

#User I/O
def choice(default="y"):
    if (default == "y"):
        yes = ['yes', 'y', 'ye', '']
        no = ['no', 'n']
    else:
        yes = ['yes', 'y', 'ye']
        no = ['no', 'n', '']

    choice = input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")

#Returns location of itself
def _getLocation():
    return os.path.dirname(inspect.stack()[0][1])

#loads dynamicly Hashtyps from hashlib
def cracker(hashTyp, hash, wordlist):

    moduleLoader = __import__('hashlib', fromlist=[hashTyp])
    hashClass = getattr(moduleLoader, hashTyp)


    print("\n---------------------Parameters ---------------------")
    print('Hash:', hash)
    print('Wordlistpath:', wordlist)
    print("\n---------------------Start cracker---------------------")

    counter = 0
    clockStart = clock()
    with open(wordlist,"r") as f:
        for line in f:
            counter += 1

            if counter % 500000 == 0:
                print(counter, "Hashes calculated")

            calc = hashClass(line.encode()).hexdigest()

            if hash == calc:
                print("\n============Result================\n\nYour Password is", line)
                break
        else:
            print("\nNo Hash found! Maybe try another wordlist.")
    clockEnd = clock()

    runTime = clockEnd - clockStart
    print("\nHad to try {0} Hashes.\nCalculated {1:.4f} Seconds.".format(counter,runTime))



def _callCracker(hash, hashTyp):
    print("Your hash might be a {0}.\n\n\nDo you wish to crack the hash? (Y/n)".format(hashTyp))
    if (choice()):
        print("Do you want to use the default wordlist? (Y/n)")

        if (choice()):
            cracker(hashTyp, hash, os.path.join(_getLocation(), "wordlist", "default.txt"))
        else:
            print("Please insert your wordlist:")
            cracker(hashTyp, hash, input())

#idetifies with the lenght of the hash which typ it is
#TODO: this can be done better
def identifiy(hash):
    print("\n---------------------Parameters ---------------------")
    print('Hash:', hash)
    print("\n---------------------Identifier---------------------")
#whirelpool:128,...
    hashBiblio={32:"md5",40:"sha",64:"sha256",128:"sha512"}

    try:
        _callCracker(hash,hashBiblio[len(hash)])
    except:
        print("Unknown hash")

