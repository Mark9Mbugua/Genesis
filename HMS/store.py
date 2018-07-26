#getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        #ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        #displaying the logs in the right frame
        self.logs = Label(self.right, text="Logs", font=('arial 20 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)
        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=35)
        self.box.insert(END, "Total Appointments till now: " + str(self.final_id))






self.box.insert(END, "Appointment fixed for " +str(self.val1) +"at " +str(self.val5))
