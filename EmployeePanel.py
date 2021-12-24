from tkinter import *
from tkinter import messagebox

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

        # Frame 2:
        self.frame2 = Frame(self)
        self.frame2.pack()

        reportSelections = ["(1) Which employee makes the hightest number of reservations?" 
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
    window = ManagerPanel()
    window.mainloop()