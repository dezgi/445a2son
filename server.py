import socket,threading


class ClientThread(threading.Thread):

    def __init__(self,clientAddress,clientSocket):
        threading.Thread.__init__(self)
        self.clientAddress =clientAddress
        self.clientSocket = clientSocket
        print("New connection is added!")

    def run(self):
        print("Connection from ",self.clientAddress)
        msg = "SERVER >>> Connection successful!".encode()
        self.clientSocket.send(msg)
        clientMsg = self.clientSocket.recv(1024).decode()  # get client message
        print("Client message username and password:", clientMsg)

        while clientMsg!= "CLIENT >>> TERMINATE":
            print("Client meessage", clientMsg)
            msg = ("SERVER >>>" + clientMsg.replace("CLIENT >>>" , "")).encode()
            self.clientSocket.send(msg)
            clientMsg = self.clientSocket.recv(1024).decode()

        msg = "SERVER >>> TERMINATE".encode() # server message
        self.clientSocket.send(msg)
        print("Connection terminated - ",self.clientAddress)
        connection.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 500
    mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    try:
        mySocket.bind((HOST,PORT))
    except socket.error:
        print("Call to bind failed!")
        exit(1)
    while True:
        print("Waiting for connection...")
        mySocket.listen()
        connection, address = mySocket.accept()
        newthread = ClientThread(address,connection)
        newthread.start()