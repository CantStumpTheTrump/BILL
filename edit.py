import sys
import os
counter = 0
if len(sys.argv) > 1: 
		print("Welcome to Bill, the world's most minimal editor")
		file = open(sys.argv[1],"a+")
		print("opened "+sys.argv[1]+" for appending")
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
				if "y" in exit:
					sys.exit()
				elif "n" in exit:
					pass
	
else:
	print("Welcome to Bill, the world's most minimal editor. Ctrl C to quit")
	filename = raw_input("filename:")
	open = open(filename,"a+")
	while True:
		try:
			counter+=1
			content = raw_input(counter)
			open.write(content+"\r\n")
		except KeyboardInterrupt:
				sys.exit()
