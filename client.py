import socket
from tkinter import *
from tkinter import messagebox



class LoginScreen(Frame):

    def __init__(self, client):
        Frame.__init__(self)

        self.client = client
        self.pack(expand = YES, fill = BOTH)

        self.master.title("Login")
        self.master.geometry("400x200")

        serverMsg = self.client.recv(1024).decode()

        # Frame1 : userName
        self.frame1 = Frame(self)
        self.frame1.pack(padx=5,pady=5)

        self.userNameLabel = Label(self.frame1, text="User name")
        self.userNameLabel.pack(side = LEFT, padx= 5, pady=5)

        self.userName = Entry(self.frame1, name="username")
        self.userName.pack(side = LEFT, padx=5, pady=5)

        # Frame2 : password
        self.frame2 = Frame(self)
        self.frame2.pack(padx=5,pady=5)

        self.passwordLabel = Label(self.frame2, text="Password")
        self.passwordLabel.pack(side = LEFT, padx= 5, pady=5)

        self.password = Entry(self.frame2, name="password", show="*")
        self.password.pack(side = LEFT, padx=5, pady=5)

        # Frame2 : login button
        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.login = Button(self.frame3, text="Login", command=self.buttonPressed)
        self.login.pack(side = LEFT, padx= 5, pady=5)

    def buttonPressed(self):
        #username = self.userName.get("1.0", END)[0:-1]
        username = self.userName.get()
        password = self.password.get()
        loginstr = "login"
        add_ = ";"
        loginstr = loginstr + add_ + username + add_ + password
        encodedstr = loginstr.encode()
        self.client.send(encodedstr) # send the client message to the server

        serverMsg = self.client.recv(1024).decode()

        if serverMsg == "SERVER >>> TERMINATE":
            self.master.destroy()
        else:
            print(serverMsg)
        #return loginstr
        #print(loginstr)
        #checkServer(loginstr)

    def checkServer(loginstr):
        file = open("users.txt")  # opens file
        lines = file.readlines()
        username = loginstr.split(";")[1]
        password = loginstr.split(";")[2]
        userlist = []
        for line in lines:
            userdetails = line.split(";")
            userlist.append(
                userdetails)  # ['employee1', 'e123', 'employee\n'] adds username,password and role to the userlist
        i = 0
        while (i < len(
                userlist)):  # checks all the users if there is a match in username and password it stops, otherwise it continues until check all the data
            notfound = 0
            if (userlist[i][0] == username):
                if (userlist[i][1] == password):
                    if (userlist[i][2] == "employee\n"):
                        messagebox.showinfo("Message", "Login successful\n" + "Welcome " + username)
                        print("this user is employee")
                        break
                        # goemployee gui
                    else:  # if the user is not specified as employee it means they are manager
                        print("this user is manager")
                        messagebox.showinfo("Message", "Login successful\n" + "Welcome " + username)
                        # gomanager gui
                else:
                    print("Password is incorrect!")
            else:
                print("User not found!")
                notfound = 1
            i = i + 1
        if notfound == 1:
            messagebox.showinfo("Message", "Invalid credentials\n", icon='error')  # change icon to the error icon

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
    mySocket.close()

    #serverMsg = mySocket.recv(1024).decode()


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