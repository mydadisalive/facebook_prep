#!/usr/bin/python3

import requests

# GET
ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
print(r.url)

# POST
pload = {'username':'olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)

#print(r.text)
#print(r.json())

r_dict = r.json()
#print(r_dict['form']['username'])