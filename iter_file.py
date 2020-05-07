#!/usr/bin/python3

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

with open('bla.txt') as f:
	for chunk in read_in_chunks(f,3):
		print(chunk, end='')