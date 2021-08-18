import cv2
import imutils
import socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostbyname()
host_ip = socket.gethostbyname(host_name)
print(host_ip)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
print('listening at:', socket_address)

vid = cv2.VideoCapture("home\aman\vid.mp4")
fps, st, frames_to_count, cnt = (0,0,20,0)

while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ', client_addr)
    print(msg)