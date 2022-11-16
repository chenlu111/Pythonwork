import os
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1',7000))

filename = c.recv(1024).decode('utf-8')
print('The server requests my file:',filename)
if os.path.exists(filename):
    print('I have %s, begin to download!' % filename)    
    size = 1024
    with open(filename,'rb') as f:
        while True:
            data = f.read(size)
            c.send(data)
            if len(data) < size:
                break
    print('%s is downloaded successfully!' % filename)
else:
    print('Sorry, I have no %s' % filename)
    c.send(b'no')
data = c.recv(1024)
print(data.decode('utf-8'))

c.close()
