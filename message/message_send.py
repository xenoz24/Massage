import socket
import server

def send(mes_send):
    while True:
        data = input("輸入文字:")
        if data == 'exit':
            mes_send.close()
            break
        else:
            mes_send.send(data.encode())