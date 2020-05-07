#!/usr/bin/python3

from pprint import pprint


#{ 
#    name1: { LEG_LENGTH : "1.2", STRIDE_LENGTH ="1.3", "DIET" : "x", STANCE = "bipedal" },
#    name1: { LEG_LENGTH : "1.2", STRIDE_LENGTH ="1.3", "DIET" : "x", STANCE = "bipedal" },
#    name1: { LEG_LENGTH : "1.2", STRIDE_LENGTH ="1.3", "DIET" : "x", STANCE = "bipedal" }
#}


import csv

g = 9.8      # gravitional const

def speed(dino):
    ''' return dino speed'''
    return (float(d[dino]['STRIDE_LENGTH']) / float(d[dino]['LEG_LENGTH']) - 1) * (float(d[dino]['LEG_LENGTH']) * g)**0.5

def csvToDict(filename,d):
    ''' convert csv and add its contents to dictionary d'''
    with open(filename) as f:
        for line in csv.DictReader(f):
            name = line['NAME']
            if name not in d:
                d[name] = line
                del d[name]['NAME']
            else:
                d[name] = { **d[name], **line }

# main
d = {}
csvToDict("dataset1.csv", d)
csvToDict("dataset2.csv", d)

bipedals = [ dino for dino in d.keys() if 'STANCE' in d[dino] and d[dino]['STANCE'] == "bipedal" ]
bipedals_stride_leg_length = [ dino for dino in bipedals if 'LEG_LENGTH' in d[dino] and 'STRIDE_LENGTH' in d[dino] ]
sorted_by_speed_bipedals = sorted(bipedals_stride_leg_length, key=speed)
print(sorted_by_speed_bipedals)
