import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',6666))
s.listen(1)

while True:
    print("server is waiting...")
    conn, addr = s.accept()
    
    while True:
        
        data_json = conn.recv(1024)  
        data = json.loads(data_json.decode())
        print("data:", data)
        file_size = data["params"]["file_size"]
        file_name = data["params"]["file_name"]

       
        receive_data_len = 0
        with open("" + file_name,"wb") as f:

            while receive_data_len < file_size:
                temp = conn.recv(1024)
                f.write(temp)
                receive_data_len += len(temp)

        print("successfully")