
from tkinter import *
from tkinter import messagebox
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