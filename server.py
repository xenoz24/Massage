import socket
import threading

serversocket = None
host = None
port = None
# create a socket object
def socket_set():
    global serversocket,host,port
    serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)

def con():
    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        while True:
            data = input("say something")
            if data == 'exit':
                clientsocket.close()
                break
            info = clientsocket.send(data.encode())

            recivemsg = clientsocket.recv(1024)
            if recivemsg != '':
                print(recivemsg.decode('utf-8'))


if __name__ == "__main__":
    socket_set()
    con()