#!/usr/bin/env python
from os import system
import sys
system("clear")
counter = 0
print("Welcome to Bill, the world's most minimal editor  ")
def commandmode():  # How'd it get burned
   while True:
       command = raw_input(">")
       if "killbill" in command:
           sys.exit()
       elif "return" in command:
        break
       elif "help" in command:
        print("Bill Commands\r\n1: 'Help' - prints this text\r\n 2: 'Return' - returns to editing mode from command mode\r\n 3: 'killbill' - Exits the editor")
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = raw_input("filename:")

file = open(filename, "a+")
print "opened " + filename + " for editing"

for line in file:
    counter += 1
    print counter, line.strip()

while True:
    try:
        counter += 1
        input = raw_input(counter)
        file.write(input + "\r\n")
    except(KeyboardInterrupt):
        commandmode()
