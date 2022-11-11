import socket
import os
import json

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1',6666))
while True:
    params = input('Enter the file name you want')
    cmd,local_path = params.split("")
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    file_params = {file_name,file_size,}
    data = {cmd,file_params}
    print(data)

    c.send(json.dumps(data).encode())

    with open(local_path, "rb") as f:
        for line in f:
            c.send(line)

    print("文件发送完毕")