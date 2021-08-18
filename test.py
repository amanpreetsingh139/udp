# import socket
# import sys
#
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     print("Socket successfully created")
# except socket.error as err:
#     print("socket creation failed with error %s" % err)
#
# port = 80
#
# try:
#     host_ip = socket.gethostbyname('www.google.com')
# except socket.gaierror:
#     print("there was an error resolving the host")
#     sys.exit()
#
# s.connect((host_ip, port))
# print("the socket has successfully connected to google")


# import socket
# import sys
#
# host = ''
# port = 8888
# port = 5000
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("", port))
# print('waiting on port:', port)
# while True:
#     data, addr = s.recvfrom(1024)
#     print(data)

from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is ready to receive requests from clients')
while True:
    messagefromclient, clientaddress = server_socket.recvfrom(2048)
    print('Message from client: ', messagefromclient)
    messagetoclient = input('Enter reply messsage to client: ')
    messagetoclient = messagetoclient.encode()
    server_socket.sendto(messagetoclient, clientaddress)