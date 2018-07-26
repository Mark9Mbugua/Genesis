import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass

class StudentDB(BoxLayout):
    #object propreties that we need
    first_name_text_input = ObjectProperty() #allows us to access/manipulate info in first_name_text...
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    #fns we need
    def submit_student(self):
       #get the students name from textInput
       student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

       #add to ListView
       self.student_list.adapter.data.extend([student_name])

       #Reset ListView
       self.student_list._trigger_reset_populate()

    def delete_student(self):
        # If a list item is selected
        if self.student_list.adapter.selection:
           
            #Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
           
            # Remove the maching item
            self.student_list.adapter.data.remove(selection)

            # Reset the ListView
            self.student_list._trigger_reset_populate()  

    def replace_student(self):
        # If a list item is selected
        if self.student_list.adapter.selection:

            #Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the maching item
            self.student_list.adapter.data.remove(selection)
            
            #get the students name from textInput
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

            #add to ListView
            self.student_list.adapter.data.extend([student_name])
            
            # Reset the ListView
            self.student_list._trigger_reset_populate()

          


class StudentDBApp(App):
    def build(self):
        return StudentDB()

dbApp = StudentDBApp()
dbApp.run()        


