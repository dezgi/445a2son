import socket
from tkinter import *
from tkinter import messagebox
from LoginScreen import *
from employeegui import *

if __name__ == "__main__":

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

    window = LoginScreen(mySocket)
    window.mainloop()
    serverMsg = mySocket.recv(1024).decode()
    print("\nsuan burdayımmmm: ",serverMsg)
    if serverMsg!="loginfailure":
        window.destroy()
        employee_window = employeegui(mySocket)
        employee_window.mainloop()
        mySocket.close()


#while serverMsg != "SERVER >>> TERMINATE":

  #  window.mainloop()
    #loginObject = LoginScreen()
    #msg = loginObject.userName
  #  print(serverMsg)
    #msg = input("CLIENT >>> ")
   # msg = window.buttonPressed()
  #  print("Button pressed function message: ",msg)
    #msg = ("CLIENT >>> " + msg).encode()
    #mySocket.send(msg)
    #serverMsg = mySocket.recv(1024).decode()

#msg = "CLIENT >>> TERMINATE".encode()
#mySocket.send(msg)
#print("Connection terminated")
#mySocket.close()

