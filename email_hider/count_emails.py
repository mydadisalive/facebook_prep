#!/usr/bin/python3

# example
# brute force
# optimize
# edge case
# complexity
# miscS

# count number of email addresses in a file

import re
import sys
import os

def usage():
	print("usage: " + os.path.basename(sys.argv[0]) + " <filename>")

if len(sys.argv) != 2:
	usage()
	sys.exit(1)

filename = sys.argv[1]
try:
	f = open(filename)
	file_contents = f.read()
	email_regex = r'[\w]+@[\w]+.[\w]+'
	print(re.findall(email_regex, file_contents))
	
except:
	print("Exception occurred")
	sys.exit(1)
finally:
	f.close()
