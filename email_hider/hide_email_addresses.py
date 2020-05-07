#!/usr/bin/python3

# this script hides email addresses from a text file

import sys
import os
import re

def usage():
    print(os.path.basename(sys.argv[0]), "<text_file>")

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    usage()
    sys.exit(1)

file = sys.argv[1]

with open(file, 'r') as f:
    file_contents = f.read()

file_contents_emails_hidden = re.sub(r'[\w.-]+@[\w.-]+\.\w+','EMAIL_HIDDEN',file_contents)

with open(file, 'w') as f:
    f.write(file_contents_emails_hidden)