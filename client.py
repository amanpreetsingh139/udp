# import socket
# import sys
# import json
#
# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# server_address = ('localhost', 10000)
# message = b'Hey aman this side This is the message.  It will be repeated.'
# try:
#
#     # Send data
#     print('sending {!r}'.format(message))
#     sent = sock.sendto(message, server_address)
#
#     # Receive response
#     print('waiting to receive')
#     data, server = sock.recvfrom(4096)
#     print('received {!r}'.format(data))
#
# finally:
#     print('closing socket')
#     sock.close()
from socket import *
import json

servername = '192.168.1.191'
serverport = 4040
clientsocket = socket(AF_INET, SOCK_DGRAM)
messagetoserver = input('Enter message for server: ')
with open('/home/aman/Downloads/600.json') as f:
    data = json.load(f)
# print('data{}'.format(data))
a=json.dumps(data, indent=4, sort_keys=True)
# print(a)
# print(type(a))
clientsocket.sendto(a.encode(), (servername, serverport))
messagefromserver, serveraddress = clientsocket.recvfrom(100000)
print('Reply from server: ', messagefromserver)
clientsocket.close()
