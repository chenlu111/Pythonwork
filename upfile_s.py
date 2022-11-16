import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',7000))
s.listen(1)
print('Waiting for connecting...')

filename = 'C:/aaa.txt'
print('I want to get the file %s!' % filename)

c,addr=s.accept()
c.send(filename.encode('utf-8'))

myfile = c.recv(1024).decode('utf-8')
if myfile=='no':
    print('To get the file %s is failed!' % filename)
else:
    c.send(b'I am ready!')
    temp=filename.split('/')
    myname = 'my1_' + temp[len(temp)-1]
    size=1024
    with open(myname,'wb') as f:
        while True:
            data = c.recv(size)
            f.write(data)
            if len(data)<size:
                break
    print('The downloaded file is %s.' % myname)

s.close()