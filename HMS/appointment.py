# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database
conn = sqlite3.connect('database.db')
#cursor to move around the database
c = conn.cursor()

#empty list to later append the ids from the database
ids=[]

#tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        #creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        #labels for the window
        self.heading = Label(self.left, text="106Matic Hospital Appointments", font=('arial 30 bold'), fg="black", bg="light green")
        self.heading.place(x=0, y=0)

        #patient's name
        self.name = Label(self.left, text="Patient's name", font=('arial 15 bold'), fg="black", bg="light green")
        self.name.place(x=0, y=100)


        #age
        self.age = Label(self.left, text="Age", font=('arial 15 bold'), fg="black", bg="light green")
        self.age.place(x=0, y=140)

        #gender
        self.gender = Label(self.left, text="Gender", font=('arial 15 bold'), fg="black", bg="light green")
        self.gender.place(x=0, y=180)

        #location
        self.location = Label(self.left, text="Location", font=('arial 15 bold'), fg="black", bg="light green")
        self.location.place(x=0, y=220)

        #Appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 15 bold'), fg="black", bg="light green")
        self.time.place(x=0, y=260)

        #phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 15 bold'), fg="black", bg="light green")
        self.phone.place(x=0, y=300)

        # Entries for all the Labels
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        #button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, bg='steelblue', command= self.add_appointment)
        self.submit.place(x=300, y=330)

    #function to call when the submit button is clicked
    def add_appointment(self):
         #getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='':
            tkinter.messagebox.showinfo("warning", "Please fill up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success!", "Appointment for " +str(self.val1)+ " has been created")

        
       
#creating the object
root = Tk()
b = Application(root)

#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False, False)

