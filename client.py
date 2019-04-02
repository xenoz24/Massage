import time
import socket
import server
import threading

s = None
host = None
port = None
clientname = None
def socket_set():
    global s,host,port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))

def recive():
    while True:
        msg = s.recv(1024)
        if not msg:
            pass
        else:
            print('伺服器: %s' % msg.decode('utf-8') + '\n')

def send():
    clientname = 'aa'

    while 1:
        sendmsg = input('%s send:' % clientname)
        if sendmsg == 'exit':
            s.close()
            break
        s.send(sendmsg.encode())


if __name__ == '__main__':
    socket_set()
    send_thread = threading.Thread(target=send)
    send_thread.start()
    recive_thread = threading.Thread(target=recive)
    recive_thread.start()