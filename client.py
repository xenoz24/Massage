import socket
import server

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
    print(s)
    receive = server.receiveThread.run(s)
    print(receive)
    receive.start()
    send = server.sendThread.run(s)
    send.start()

if __name__ == '__main__':
    main()