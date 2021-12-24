import socket

HOST = "127.0.0.1"
PORT = 500
print("Attempting connection")
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    mySocket.connect((HOST,PORT))
except:
    print("Call to connect failed!")
    exit(1)
print("Connected to server")

serverMsg = mySocket.recv(1024).decode()

while serverMsg != "SERVER >>> TERMINATE":
    print(serverMsg)
    msg  = input("CLIENT >>> ")
    msg = ("CLIENT >>> " + msg).encode()
    mySocket.send(msg)
    serverMsg = mySocket.recv(1024).decode()

msg = "CLIENT >>> TERMINATE".encode()
mySocket.send(msg)
print("Connection terminated")
mySocket.close()