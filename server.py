import socket
import threading
from message import message_send
from message import message_receive

host = None
port = None

class MyThread(threading.Thread):
    def __init__(self,threadName,num):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.num = num

    def send(self,con):
        message_send.send(con)
    def receive(self,con):
        message_receive.receive(con)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        server_thread = MyThread('name',1)
        server_thread.start()
        server_thread.receive(conn)
        server_thread.send(conn)


if __name__ == "__main__":
    main()