#!/usr/bin/python3

import socket

ip_port_list = [("127.0.0.1",80), ("127.0.0.1",81)]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for ip_port in ip_port_list:
    ip,port = ip_port
    try:
        s.connect((ip,port))
    except:
        print("error opening ",ip,port)
    finally:
        s.close()


