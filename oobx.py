#!/usr/bin/python3
import socket
import sys

HOST = '0.0.0.0'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind socket
try:
        s.bind((HOST, PORT))
except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

print('Socket bind complete')

#Start listening on socket
s.listen(10)
print('Socket now listening')

# Talk with client
while 1:
    #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected')
        print ('Destination address & port:', addr )
        
        while True:
                dataFromClient = conn.recv(1024)
                print(dataFromClient.decode('utf-8'))
                if not dataFromClient:
                        print("[Client] Disconnected\n")
                        break


        conn.sendall(dataFromClient)
s.close()
