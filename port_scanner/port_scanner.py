#!/usr/bin/python3

# port scanner

import socket
from queue import Queue
from threading import Thread, Lock

# FUNCTIONS
def checkIpPort(job):
    mutex.acquire()
    ip, port, open_ports = job
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("checking ip", ip, "with port", port,": ",end='')
    try:
        con = s.connect((ip, port))
        open_ports += [(ip, port)]
        s.close()
        print("open")
    except:
        print("close")
    finally:
        mutex.release()
        
def worker():
    while True:
        job = q.get()
        checkIpPort(job)
        q.task_done()

# VARS
NUM_THREADS = 30            # number of threads to run jobs

ips = [ "127.0.0.1" ]       # set your ip range here, TBD: add ability to read from file
ports = range(100)          # set your port range here, TBD: add ability to read from file
open_ports = []             # the open ip and ports will be collected here as tuples of the form (ip,port)

mutex = Lock()

# MAIN
 

q = Queue()

# create NUM_THREADS threads
for x in range(NUM_THREADS):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

# create jobs from threads
for ip in ips:
    for port in ports:
        q.put((ip, port, open_ports))            
        
q.join()

print(open_ports)