import sys
import os
import struct

def send(s):
    file = open('cat.jpg','rb')
    filesize = os.path.getsize('cat.jpg')
    sizepack = struct.pack('i',filesize)
    s.send(sizepack)
    while True:
        data = file.read(10240)
        if not data:
            print('傳送完成')
            file.close()
            sys.exit(0)
        else:
            #print('傳送中')
            s.send(data)

def receive(conn):
    filesize = conn.recv(4)
    size, = struct.unpack('i',filesize)
    receive_size = 0
    newfilename = open('b.jpg', 'wb')
    while receive_size < size:
        recivemsg = conn.recv(10240)
        newfilename.write(recivemsg)
        receive_size += len(recivemsg)
    print('接收完成')
    sys.exit(0)