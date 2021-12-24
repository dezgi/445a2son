import socket,threading
from tkinter import *
from tkinter import messagebox
from employeegui import *
from LoginScreen import *
def checkusertxt(loginstr):
        file = open("users.txt")  # opens file
        lines = file.readlines() 
        username = loginstr.split(";")[1]
        password = loginstr.split(";")[2]
        userlist = []
        for line in lines:
            userdetails = line.split(";")
            userlist.append(userdetails) # ['employee1', 'e123', 'employee\n'] adds username,password and role to the userlist
        i=0
        while(i<len(userlist)): #checks all the users if there is a match in username and password it stops, otherwise it continues until check all the data
            notfound=0
            if(userlist[i][0]==username): 
                if(userlist[i][1]==password):
                    if(userlist[i][2]=="employee\n"):
                        print("this user is employee")
                        msg = "loginsuccess;"+username+";employee"
                        return msg
                            
                    else: #if the user is not specified as employee it means they are manager
                        print("this user is manager")
                        msg = "loginsuccess;"+username+";manager"
                        #gomanager gui
                else:
                    print("Password is incorrect!")
            else:
                print("User not found!")
                notfound = 1
            i = i+1
        if notfound ==1:
            msg = "loginfailure"
        return msg
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
        msg =checkusertxt(clientMsg)
        if msg=="loginfailure":
            messagebox.showinfo("Message", "Invalid credentials\n", icon='error')  # change icon to the error icon
        else:
            messagebox.showinfo("Message", "Login successful\n" + "Welcome ")
        print("Client meessage", clientMsg)
        encodedmsg = msg.encode()
        self.clientSocket.send(encodedmsg)
        

        
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