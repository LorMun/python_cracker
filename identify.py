#!/usr/bin/python
import os
import inspect
import importlib.util


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


def _getLocation():
    return os.path.dirname(inspect.stack()[0][1])


def _callCracker(hash, hashTyp):
    print("Your hash might be a {0}.\n\n\nDo you wish to crack the hash? (Y/n)".format(hashTyp))
    if (choice()):
        print("Do you want to use the default wordlist? (Y/n)")

        spec = importlib.util.spec_from_file_location("module.name", os.path.join(_getLocation(),"biblio","crack_{0}.py".format(hashTyp)))
        loadmodul = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(loadmodul)

        if (choice()):
            loadmodul.Cracker(hash, os.path.join(_getLocation(), "wordlist", "default.txt"))
        else:
            print("Please insert your wordlist:")
            loadmodul.Cracker(hash, input())


def identifiy(hash):
    print("\n---------------------Parameters ---------------------")
    print('Hash:', hash)
    print("\n---------------------Identifier---------------------")
    found = 0
    if len(hash) == 32:
        found = 1
        _callCracker(hash,"md5")

    if len(hash) == 40:
        found = 1
        _callCracker(hash,"sha1")

    if (not (found)):
        print("Unknown hash")
