#!/usr/bin/python3

import csv

G = 9.8 # gravitational constant

def calcSpeed(dino_name):
    dino_attributes = d[dino_name]
    if 'STRIDE_LENGTH' not in dino_attributes or 'LEG_LENGTH' not in dino_attributes:
        return(-1)
    speed = ((float(dino_attributes['STRIDE_LENGTH']) / float(dino_attributes['LEG_LENGTH'])) - 1) * (float(dino_attributes['LEG_LENGTH'])**0.5 * G)
    return speed

def csvToDict(reader, d):
    for row in reader:
        name = row['NAME']
        if name not in d:
            d[name] = {}
        
        for key in row.keys():
            if key=="NAME":
                continue
            else:
                d[name][key]    = row[key]

#speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
with open('dataset1.csv','r') as f1, open('dataset2.csv','r') as f2:
    reader1 = csv.DictReader(f1)
    reader2 = csv.DictReader(f2)
    
    d={}

    csvToDict(reader1, d)
    csvToDict(reader2, d)

    bipedals = [ dino for dino in d.keys() if 'STANCE' in d[dino] and d[dino]['STANCE'] == 'bipedal' ]
    print(bipedals)
    print('bipedals sorted by speed:', sorted(bipedals, key=calcSpeed))