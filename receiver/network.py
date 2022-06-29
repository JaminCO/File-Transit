import socket
import random

class Sender:
    def create_server():
        global s
        host = socket.gethostname()#socket.gethostbyname(socket.gethostname())
        port = random.randrange(1001, 9999)

        s = socket.socket()
        s.bind((host, port))

        s.listen(1)

        return host, port, s

    def accept_connection(s):
        global conn, addr
        conn, addr = s.accept()

        return conn, addr

    def send(file_path, file_name, conn):
        # file_name = input("File name :")
        filename_data = conn.send(file_name.encode("utf-8"))
        if conn == "":
            return "Not connected to a client"
        else:
            file = open(file_path, 'rb')
            file = file.read()
            print(len(file))
            data = conn.send(file)
            print(data)
            confirmation = (conn.recv(8192)).decode("utf-8")
            if confirmation == "True":
                return "File sent successfully"
            else:
                return "Transfer Unsuccessfull"
    def close(s):
        s.close()

class Reciever:
    def connect(host, port):
        global s, data_size
        s = socket.socket()
        s.connect((host, port))
        data_size = 1000000000000

        return s

    def recieve(s, data_size=100000000):
        file_name = s.recv(data_size).decode("utf-8")
        # print("file name recieved")
        file = open(file_name, 'wb')
        data = s.recv(data_size)
        file.write(data)
        file.close()
        print(len(data))
        confirmation = s.send("True".encode("utf-8"))
        file = open(file_name, 'rb')
        print(len(file.read()))
        return "File Recieved",file_name
    def close(s):
        s.close()