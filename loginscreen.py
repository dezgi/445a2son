from tkinter import *
from tkinter import messagebox
class LoginScreen(Frame):
    def __init__(self, client):
        Frame.__init__(self)

        self.client = client
        self.pack(expand = YES, fill = BOTH)

        self.master.title("Login")
        self.master.geometry("400x200")

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