import server
import socket

def receive(mes_rev):
    while True:
        recivemsg = mes_rev.recv(1024)
        print(recivemsg.decode('utf-8') + '\n')

