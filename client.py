
import socket

s = None
host = None
port = None
def socket_set():
    global s,host,port
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))
def con():
    while True:
        sendmsg = input('send:')

        if sendmsg == 'exit':
            s.close()
            break
        info = s.send(sendmsg.encode())
        msg = s.recv(1024)
        if not msg:
            pass
        else:
            print(msg.decode('utf-8'))

if __name__ == '__main__':
    socket_set()
    con()