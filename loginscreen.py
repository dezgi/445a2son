from tkinter import *
from tkinter import messagebox

class LoginScreen(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
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
class EmployeePanel(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Employee")

        # Frame1 : apartmentCode
        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.apartmentCodeLabel = Label(self.frame1, text = "Apartment Code")
        self.apartmentCodeLabel.pack(side = LEFT,padx = 5, pady=5)

        self.apartmentCode = Entry(self.frame1, text = "apartmentCode")
        self.apartmentCode.pack(side = LEFT,padx = 5, pady=5)

        # Frame2 : startDate
        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.startDateLabel = Label(self.frame2, text="Start Date")
        self.startDateLabel.pack(side=LEFT, padx=5, pady=5)

        self.startDate = Entry(self.frame2, text="startDate")
        self.startDate.pack(side=LEFT, padx=5, pady=5)

        # Frame3 : endDate
        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.endDateLabel = Label(self.frame3, text="End Date")
        self.endDateLabel.pack(side=LEFT, padx=5, pady=5)

        self.startDate = Entry(self.frame3, text="endDate")
        self.startDate.pack(side=LEFT, padx=5, pady=5)

        # Frame4 : customerName
        self.frame4 = Frame(self)
        self.frame4.pack(padx=5, pady=5)

        self.customerNameLabel = Label(self.frame4, text="Customer Name")
        self.customerNameLabel.pack(side=LEFT, padx=5, pady=5)

        self.customerName = Entry(self.frame4, text="customerName")
        self.customerName.pack(side=LEFT, padx=5, pady=5)

        # Frame5 : show button
        self.frame5 = Frame(self)
        self.frame5.pack(padx=5, pady=5)

        self.showButton = Button(self.frame5, text="Show", command=self.buttonPressedShow)
        self.showButton.pack(side=LEFT, padx=5, pady=5)

        #Frame6 : reserve button
        self.frame6 = Frame(self)
        self.frame6.pack(padx=5, pady=5)

        self.reserveButton = Button(self.frame6, text="Reserve", command=self.buttonPressedReserve)
        self.reserveButton.pack(side=LEFT, padx=5, pady=5)

    def buttonPressedShow(self):
        apartmentCode = self.apartmentCode.get()
        startDate = self.startDate.get()
        endDate = self.startDate.get()
        customerName = self.customerName.get()

        messagebox.showinfo("Message", "Succesfull\n" + "Apartment Code:" + apartmentCode + "\nStart Date" + startDate
                            + "\nEnd Date" + endDate + "\nCustomer Name:" + customerName)
    def buttonPressedReserve(self):
        messagebox.showinfo("Message", "Reserve Button is succesfully working .. \n")

class ManagerPanel(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Manager")

        # Frame1 : report selection label
        self.frame1 = Frame(self)
        self.frame1.pack(padx = 5, pady=5)

        self.reportSelectionLabel = Label(self.frame1, text = "Select your report:")
        self.reportSelectionLabel.pack(side = LEFT,padx = 5, pady=5)

        # Frame 2: Radio Buttons
        self.frame2 = Frame(self)
        self.frame2.pack()

        reportSelections = ["(1) Which employee makes the hightest number of reservations?",
            "(2) Which apartment is the most popular?",
            "(3) How many apartmnets are currently avaliable?",
            "(4) How many apartments ahve not been reserved yet?"]

        self.chosenReport = StringVar()
        self.chosenReport.set(reportSelections[ 0 ])

        # create RadioButtons components
        for i in reportSelections:
            button_ = Radiobutton(self.frame2, text = i,
                                  variable = self.chosenReport,
                                  value = self.selectReport)
            button_.pack(padx=5,pady=5)

        # Frame 3: request button
        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.requestButton = Button(self.frame3, text="Request", command=self.buttonPressedRequest)
        self.requestButton.pack(side = LEFT, padx= 5, pady=5)

        # Frame 4: close button
        self.frame4 = Frame(self)
        self.frame4.pack(padx=5, pady=5)

        self.closeButton = Button(self.frame4, text="Close", command=self.buttonPressedClose)
        self.closeButton.pack(side = LEFT, padx= 5, pady=5)


    def buttonPressedRequest(self):
        messagebox.showinfo("Message", "Request button is working successfully. \n")

    def buttonPressedClose(self):
        messagebox.showinfo("Message", "Close button is working successfully. \n")

    def selectReport(self):
        if self.chosenReport.get() == "(1) Which employee makes the hightest number of reservations?":
            messagebox.showinfo("Message", "Report1 is selected. \n")
        elif self.chosenReport.get() == "(2) Which apartment is the most popular?":
            messagebox.showinfo("Message", "Report2 is selected. \n")
        elif self.chosenReport.get() == "(3) How many apartmnets are currently avaliable?":
            messagebox.showinfo("Message", "Report3 is selected. \n")
        elif self.chosenReport.get() == "(4) How many apartments ahve not been reserved yet?":
            messagebox.showinfo("Message", "Report4 is selected. \n")

if __name__ == "__main__":

    window = LoginScreen()
    #window = EmployeePanel()
    #window = ManagerPanel()
    window.mainloop()
