import Img
import server
import time

def send(mes_send):
    while True:
        data = input("輸入文字:")
        if data == 'exit':
            print(data)
            mes_send.send(data.encode())
            time.sleep(0.2)
            mes_send.close()
            break
        elif data == 'file':
            mes_send.send(data.encode())
            time.sleep(0.2)
            server.SendImg(mes_send).start()
        else:
            mes_send.send(data.encode())
        print('a')

def receive(msg_receive):
    while True:
        recivemsg = msg_receive.recv(1024)
        print(recivemsg)

        if recivemsg.decode('utf-8') == 'exit':
            msg_receive.close()
            break
        elif recivemsg.decode('utf-8') == 'file':
            server.ReceiveFile(msg_receive).start()
            time.sleep(1)
        else:
            print(recivemsg.decode('utf-8') + '\n')
