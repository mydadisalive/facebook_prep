#!/usr/bin/python3

# example
# brute force
# optimization
# edge cases
# complexity
# misc

g = 9.8 # gravitational const

def dinosaurSpeed(dino_name):
	''' return dinosaur speed. assumes dino is a dinosaur object with all needed records '''
	if 'STRIDE_LENGTH' not in d[dino_name] or 'LEG_LENGTH' not in d[dino_name]:
		return -1

	STRIDE_LENGTH, LEG_LENGTH = (float(d[dino_name]['STRIDE_LENGTH']), float(d[dino_name]['LEG_LENGTH']))
	
	speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * pow(LEG_LENGTH * g, 0.5)
	return speed	

with open("dataset1.csv") as f1, open("dataset2.csv") as f2:
	d = {}
	count = 0
	for line in f1.readlines():
		# skip the first line
		if count == 0:
			count += 1
			continue
		
		name, leg_length, diet = line.split(",")
		if name not in d:
			d[name] = {}
		d[name]["LEG_LENGTH"], d[name]["DIET"] = ( leg_length, diet.strip() )
		count += 1
	
	count = 0
	for line in f2.readlines():
		# skip the first line
		if count == 0:
			count += 1
			continue
		
		name, stride_length, stance = line.split(",")
		if name not in d:
			d[name] = {}
		d[name]["STRIDE_LENGTH"] , d[name]["STANCE"] = ( stride_length, stance.strip() )
		count += 1

	bipedals = [ name for name in d.keys() if 'STANCE' in d[name] and d[name]['STANCE'] == "bipedal" ]
	print(sorted(bipedals, key = dinosaurSpeed))