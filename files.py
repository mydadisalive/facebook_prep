#!/usr/bin/python3

import os

print("--- files ---")
with open('bla.txt','w') as f:
	for i in range(3):
		f.write("line "+str(i)+"\n")

with open('bla.txt') as f:
	print(f.read())

with open('bla.txt','rt') as f:
	for line in f:
		print(line,end='')
		
print("create tempfile")
f = open('tempfile','w')
f.close()

print("delete tempfile if exists")
if os.path.exists("tempfile"):
	print("tempfile exists")
	os.remove("tempfile")
else:
	print("tempfile does not exist")
	
print("delete tempfile if exists")
if os.path.exists("tempfile"):
	print("tempfile exists")
	os.remove("tempfile")
else:
	print("tempfile does not exist")

# directories
print("--- directories ---")
print("current directory is "+os.getcwd())
print("creating directory bla_dir")
try:
	os.mkdir("bla_dir", 0o755)
except OSError:
	print("creating of the directory bla_dir failed")
else:
	print("succesfully created the directory bla_dir")

os.rmdir("bla_dir")

