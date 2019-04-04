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
        print('啟動接收檔案')
        Img.revice(self.conn)

class SendImg(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        print('啟動傳檔')
        Img.send(self.conn)


def main():
    global conn
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()

    ReceiveTread(conn).start()
    SendThread(conn).start()


if __name__ == "__main__":
    main()