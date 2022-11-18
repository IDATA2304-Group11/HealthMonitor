import HealthDataGenerator
import socket

port = 8390 # Arbituary port
address = ('127.0.0.1',port)


def connect(port, adress):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(address)
    return s




