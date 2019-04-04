import server

def send(s):
    filepath = 'cat.jpg'
    file = open(filepath,'rb')
    while True:
        data = file.read()
        if not data:
            file.closed
            #s.close()
            break
        else:
            s.send(data)


def revice(conn):
    newfilename = open('b.jpg', 'wb')
    print('hi')
    while True:
        recivemsg = conn.recv(1024)
        if not recivemsg:
            newfilename.closed
            #conn.close()
            break
        else:
            newfilename.write(recivemsg)
