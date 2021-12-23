from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


class LoginScreen(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Login")

        self.frame1 = Frame(self)
        self.frame1.pack(padx=5,pady=5)

        self.userNameLabel = Label(self.frame1, text="User name")
        self.userNameLabel.pack(side = LEFT, padx= 5, pady=5)

        self.userName = Entry(self.frame1, name="username")
        self.userName.pack(side = LEFT, padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5,pady=5)

        self.passwordLabel = Label(self.frame2, text="Password")
        self.passwordLabel.pack(side = LEFT, padx= 5, pady=5)

        self.password = Entry(self.frame2, name="password", show="*")
        self.password.pack(side = LEFT, padx=5, pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.login = Button(self.frame3, text="Login", command=self.buttonPressed)
        self.login.pack(side = LEFT, padx= 5, pady=5)

    def buttonPressed(self):
        username = self.userName.get()
        password = self.password.get()

        #checkServer()
        # reading username.txt file
        file = open("users.txt")  # opens file
        lines = file.readlines()  # since there is no data in the first line, it starts reading the file after second line
        for line in lines:
            print(line)
            splitted_line = line.split(";")
            print(splitted_line)

        if username == 'ezgi' and password == '12345':
            messagebox.showinfo("Message", "Login successful\n" + "Welcome ")
        else:
            messagebox.showinfo("Message", "Invalid credentials\n",icon = 'error') # change icon to the error icon


    #def checkServer(self,a):

if __name__ == "__main__":
    window = LoginScreen()
    window.mainloop()
