from tkinter import *
from tkinter import messagebox



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
        loginstr = "login"
        add_ = ";"
        loginstr = loginstr + add_ + username + add_ +password
        print(loginstr)
        checkServer(loginstr)


def checkServer(loginstr):
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
                        messagebox.showinfo("Message", "Login successful\n" + "Welcome "+username)
                        print("this user is employee")
                        break
                            #goemployee gui
                    else: #if the user is not specified as employee it means they are manager
                        print("this user is manager")
                        messagebox.showinfo("Message", "Login successful\n" + "Welcome "+username)
                        #gomanager gui
                else:
                    print("Password is incorrect!")
            else:
                print("User not found!")
                notfound = 1
            i = i+1
        if notfound ==1:
                messagebox.showinfo("Message", "Invalid credentials\n",icon = 'error') # change icon to the error icon

                
            
        
      



        
     

    #def checkServer(self,a):

if __name__ == "__main__":
    window = LoginScreen()
    window.mainloop()
