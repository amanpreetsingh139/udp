# # importing necessary packages
# import socket
# import sys
# import json
#
# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Bind the socket to the port
# server_address = ('localhost', 10000)
# print('starting up on {} port {}'.format(*server_address))
# sock.bind(server_address)
#
# while True:
#     print('\nwaiting to receive message')
#     data, address = sock.recvfrom(1000000)
#     print('received {} bytes from {}'.format(
#         len(data), address))
#     print(data)
#
#     if data:
#         sent = sock.sendto(data, address)
#         print('sent {} bytes back to {}'.format(
#             sent, address))
from socket import *
serverport = 12000
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverport))
print('The server is ready to receive requests from clients')
while True:
    messagefromclient, clientaddress = serversocket.recvfrom(2048)
    print('message from client:', messagefromclient)
    messagetoclient = input('enter reply message to client: ')
    serversocket.sendto(messagetoclient.encode(), clientaddress)
