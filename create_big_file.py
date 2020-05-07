#!/usr/bin/python3

import os
from shutil import copyfile
import hashlib
import time

CHUNK_SIZE = 1024

KB = 1024 # 1KB
MB = 1024 * 1024 # 1MB


with open('largefile1', 'wb') as fout:
     fout.write(os.urandom(MB))

with open('largefile2', 'wb') as fout:
     fout.write(os.urandom(MB))


copyfile('largefile1', 'largefile2')

def compareFiles(file1, file2):
	with open('largefile1', 'rb') as f1, open('largefile2', 'rb') as f2:
		while True:
			x1 = f1.read(CHUNK_SIZE)
			x2 = f2.read(CHUNK_SIZE)
						
			if not x1 and not x2:
				break
				
			if x1 == x2:
				continue
			else:
				print("file are not identical")
				return False
		
		print("files "+file1+" "+file2+" are identical")
		return True

compareFiles('largefile1', 'large_file2')
