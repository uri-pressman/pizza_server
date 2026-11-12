import socket
import random
import time

HOST = '0.0.0.0'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST, port)
server.listen(1)


print("waiting for orders")
