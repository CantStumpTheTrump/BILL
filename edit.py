#!/usr/bin/env python
from os import system
import sys
system("clear")
counter = 0
print("Welcome to Bill, the world's most minimal editor  ")

if len(sys.argv)>1: filename = sys.argv[1]
else:               filename = raw_input("filename:")

file = open(filename,"a+")
print "opened "+filename+" for appending"

for line in file:
    counter+=1
    print counter,line.strip()

while True:
    try:
        counter+=1
        input = raw_input(counter)
        if "/quit" in input:
            sys.exit()
        else:
            file.write(input+"\r\n")
    except(KeyboardInterrupt):			
        exit = raw_input("\r\nAre you sure you'd like to exit? y/n")
        if "y" in exit: sys.exit()
        elif "n" in exit: pass 
