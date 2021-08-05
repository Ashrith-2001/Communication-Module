# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:22:20 2019

@author: Nikhil
"""

import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('169.254.199.57',5005))
serv.listen(999)
string=''
while True:
    print("\n in loop ")
    conn, addr = serv.accept()
    from_client = ''
    data = conn.recv(4096)
    data=data.decode('utf-8')
    from_client += data
    print (from_client)
    choice=input("\n1)To Enter the command\n2)To exit\t")
    if(choice=='1'):
        string=input()
        msg=bytes(string,'utf-8')
        conn.send(msg)
    elif(choice=='2'):
        string = '%#%#%#'
        msg=bytes(string,'utf-8')
        conn.send(msg)
        conn.close()
        break
    else:
        print("invalid input")
print ('client disconnected')