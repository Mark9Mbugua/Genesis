#import all modules
from tkinter import *
import tkinter.messagebox
import sqlite3
import datetime

conn = sqlite3.connect("store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()

#temporary lists like sessions oon the web
products_list = []
product_price = []
product_quantity = []
product_id = []

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        #frames
        self.left = Frame(master, width=700, height=768, bg="white")
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg="lightblue")
        self.right.pack(side=RIGHT)

        #components
        self.heading = Label(self.left, text="106 Fasho Shopiro", font=('arial 40 bold'), bg='white')
        self.heading.place(x=0, y=0)

        self.date_l = Label(self.right, text="Today's Date: " + str(date), font=("arial 16 bold"), bg="lightblue", fg="white")
        self.date_l.place(x=0, y=0)

        # table invoice===============================================================================
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg="lightblue", fg='white')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg="lightblue", fg='white')
        self.tquantity.place(x=250, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg="lightblue", fg='white')
        self.tamount.place(x=500, y=60)

        #Enter Stuff
        self.enterid = Label(self.left, text="Enter Product's ID", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightgrey')
        self.enteride.place(x=300, y=80)
        self.enteride.focus()

        #Button
        self.search_btn = Button(self.left, text="Search", width=22, height=2, bg="steelblue", command=self.ajax)
        self.search_btn.place(x=465, y=120)

        # Fill it later by the function Ajax
        self.productname = Label(self.left, text="", font=('árial 27 bold'), bg='white', fg='steelblue')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text='', font=('arial 27 bold'), bg='white', fg='steelblue')
        self.pprice.place(x=0, y=290)

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        # get the products info with that id and fill it in the labels above
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="Prodct's Name :" +str(self.get_name))
        self.pprice.configure(text="Price:Ksh. " +str(self.get_price))

        #create the quantity and the discount label
        #quantity
        self.quantity_l = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg="white")
        self.quantity_l.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg="lightgrey")
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        #Discount
        self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'), bg="white")
        self.discount_l.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg="lightgrey")
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        # add to cart button
        self.add_to_cart_btn = Button(self.left, text="Add To Cart", width=22, height=2, bg='steelblue', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=450)
        
        #Generate bill and change
        self.change_l = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg="white")
        self.change_l.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg="lightgrey")
        self.change_e.place(x=190, y=550)

        # Button change
        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='steelblue')
        self.change_btn.place(x=350, y=590)

        # Generate Bill Button
        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='red', fg="white")
        self.bill_btn.place(x=0, y=700)

        # total label
        self.total_l = Label(self.right, text="Total", font=('arial 40 bold'), bg='lightblue', fg="white")
        self.total_l.place(x=0, y=600)
        
    def add_to_cart(self, *args, **kwargs):
        #get the quantity value from the database
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in oue inventory.")
        else:
            #calculate the price
            self.final_price = float(self.quantity_value) * float(self.get_price)
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)
                
            
            




        
        
        

        

        
        


root = Tk()
b = Application(root)

root.geometry("1366x768+0+0")
root.mainloop()
