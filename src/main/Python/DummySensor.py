import HealthDataGenerator
import socket
import time

port = 9000 # Arbituary port
address = ('10.24.90.45',port)

packet = "2022-11-22 12:17:42;145;88;75;ABCD-EDFG-FJ78"

def sendDataInTimeframe(running_time):
    
    while running_time > 0:
        
    
        # Send data
        
        running_time -= 1
        time.sleep(1)
    
    
    
    
    



def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(address)
    return s


melding = connect()

melding.send(packet.encode("utf-8"))
