#!/usr/bin/python3

import csv
from pprint import pprint

g = 9.8 # gravitatonal speed
d = {}

def calcSpeed(dino):
	STRIDE_LENGTH, LEG_LENGTH = float(d[dino]["STRIDE_LENGTH"]), float(d[dino]["LEG_LENGTH"])

	speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * (LEG_LENGTH * g)**0.5	
	return speed

def csvToDict(csv_file, d):
	with open(csv_file) as f: 
		for row in csv.DictReader(f):
			if 'NAME' not in row:
				continue
			name = row['NAME']
			if name not in d:
				d[name] = {}
			d[name] = { **d[name], **row }	
	
csvToDict("dataset1.csv", d)
csvToDict("dataset2.csv", d)

bipedals = [ dino for dino in d.keys() if 'LEG_LENGTH' in d[dino] and 'STRIDE_LENGTH' in d[dino] and 'STANCE' in d[dino] and d[dino]['STANCE'] == "bipedal" ]
pprint(sorted([x for x in bipedals], key=calcSpeed))
#bipedals_with_lengths = [ x for x in bipedals if 'LEG_LENGTH' in x and 'STRIDE_LENGTH' in x ]
#bipedals_sorted_by_speed = sorted(bipedals_with_lengths, key=