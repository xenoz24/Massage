import socket
import server
import threading
import message

s = None
host = None
port = None

def socket_set():
    global s,host,port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))

def main():
    socket_set()

    server.SendThread(s).start()
    server.ReceiveTread(s).start()


if __name__ == '__main__':
    main()