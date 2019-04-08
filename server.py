import socket
import threading
import message
import Img

host = None
port = None
conn = None

class ReceiveTread(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn


    def run(self):
        message.receive(self.conn)

class SendThread(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        message.send(self.conn)

class ReceiveFile(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        print('\n啟動接收檔案')
        Img.receive(self.conn)

class SendFile(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        print('\n啟動傳檔')
        Img.send(self.conn)


def main():
    global conn
    s = socket.socket()
    host = socket.gethostname()
    port = 9999
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()

    ReceiveTread(conn).start()
    SendThread(conn).start()
    try:
        pass
    except(OSError):
        print('中斷連線')

if __name__ == "__main__":
    main()