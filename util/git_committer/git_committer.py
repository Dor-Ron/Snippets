#!/usr/bin/env python

from sys import argv
from os import system

def committer():
    '''Adds and commits filename(s) entered in argv[1:] to git repo'''
    message = raw_input("Enter commit message: ")
    for file in argv[1:]:
        system("git add %s" % file)
    system("git commit -m '%s'" % message)

if __name__ == "__main__":
    committer()
