import socket
import threading
from message import message_send
from message import message_receive

host = None
port = None

class receiveThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self,con):
        message_receive.receive(con)

class sendThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self,socket):
        message_send.send(socket)
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print(conn)
        print(addr)
        send = sendThread().run(conn)
        send.start()
        receive = receiveThread.run(conn)
        receive.start()
        print('a')


if __name__ == "__main__":
    main()