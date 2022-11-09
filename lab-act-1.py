"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

import cs50
import sys
import tkinter as tk
from tkinter import messagebox  

from helpers import get_name, get_house_number, get_street_vilage, get_city_municipality, get_province, get_country


# Redirect to new frame
def show_frame(frame):
    frame.tkraise()

# Check information about contact's details
def check_infos():
    print(a_country_input.get())
    pass

# Ask again if user really want to exit
def on_closing():
    if messagebox.askyesno(title="Exit?", message="Do you really want to close 'Address Book'?"):
        root.destroy()



# Configure root
root = tk.Tk()
root.geometry("500x500")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title("Address Book")

# Create frame for every functionality of the address book
main_menu = tk.Frame(root, bg="#EFF5F5")
add_contact = tk.Frame(root, bg="#EFF5F5")
edit_contact = tk.Frame(root, bg="#EFF5F5")
delete_contact = tk.Frame(root, bg="#EFF5F5")
view_contact = tk.Frame(root, bg="#EFF5F5")
search_contact = tk.Frame(root, bg="#EFF5F5")

# Create grid for every page frame
for frame in [main_menu, add_contact, edit_contact, delete_contact, view_contact, search_contact]:
        frame.grid(row=0, column=0, sticky="nsew")

# Main Menu (mm in var stands for main menu)
# Configure the number of rows and column main menu have
for number in range(8):
    main_menu.grid_rowconfigure(number, weight=1)
main_menu.grid_columnconfigure(0, weight=1)

# Title and description 
mm_title = tk.Label(main_menu, text="Main Menu", font=("Arial", 24), fg="white", bg="#497174")
mm_title.grid(row=0, column=0, sticky="NESW")

mm_description = tk.Label(main_menu, text="What do you want to do?", font=("Arial", 18), bg="#EFF5F5")
mm_description.grid(row=1, column=0, sticky="NESW")

# Buttons leading to other frames
mm_add_btn = tk.Button(main_menu, text="Add Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(add_contact))
mm_add_btn.grid(row=2, column=0, sticky="NESW")

mm_edit_btn = tk.Button(main_menu, text="Edit Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(edit_contact))
mm_edit_btn.grid(row=3, column=0, sticky="NESW")

mm_del_btn = tk.Button(main_menu, text="Delete Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(delete_contact))
mm_del_btn.grid(row=4, column=0, sticky="NESW")

mm_view_btn = tk.Button(main_menu, text="View Contacts", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(view_contact))
mm_view_btn.grid(row=5, column=0, sticky="NESW")

mm_search_btn = tk.Button(main_menu, text="Search Address Book", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(search_contact))
mm_search_btn.grid(row=6, column=0, sticky="NESW")

mm_exit_btn = tk.Button(main_menu, text="Exit", font=("Arial", 12), bg="#D6E4E5", command=on_closing)
mm_exit_btn.grid(row=7, column=0, sticky="NESW")



# Add Contact (a in var stands for add contact frame)
# Configure the number of rows and column in add contact frame
for number in range(12):
    add_contact.grid_rowconfigure(number, weight=1)

for number in range(2):
    add_contact.grid_columnconfigure(0, weight=1)

# Title and description 
a_title = tk.Label(add_contact, text="Add Contact", font=("Arial", 24), fg="white", bg="#497174")
a_title.grid(row=0, column=0, columnspan=2, sticky="NESW")

a_description = tk.Label(add_contact, text="Fill up the new contact's details.", font=("Arial", 18), bg="#EFF5F5")
a_description.grid(row=1, column=0, columnspan=2, sticky="NESW")

# Forms
# Firstname
a_firstname = tk.Label(add_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
a_firstname.grid(row=2, column=0, sticky="NESW", padx=30)

a_firstname_input = tk.Entry(add_contact, font=("Arial", 12))
a_firstname_input.grid(row=2, column=1, sticky="NESW", padx=30)

#Last Name
a_lastname = tk.Label(add_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
a_lastname.grid(row=3, column=0, sticky="NESW")

a_lastname_input = tk.Entry(add_contact, font=("Arial", 12))
a_lastname_input.grid(row=3, column=1, sticky="NESW", padx=30)

# Contact Number
a_number = tk.Label(add_contact, text="Contact Number", font=("Arial", 12), bg="#EFF5F5")
a_number.grid(row=4, column=0, sticky="NESW")

a_number_input = tk.Entry(add_contact, font=("Arial", 12))
a_number_input.grid(row=4, column=1, sticky="NESW", padx=30, pady=15)

# Address
a_address = tk.Label(add_contact, text="Address", font=("Arial", 16), bg="#EFF5F5")
a_address.grid(row=5, column=0, sticky="NESW", ipadx=10)

# House Number
a_house_no = tk.Label(add_contact, text="House Number", font=("Arial", 12), bg="#EFF5F5")
a_house_no.grid(row=6, column=0, sticky="NESW")

a_house_no_input = tk.Entry(add_contact, font=("Arial", 12))
a_house_no_input.grid(row=6, column=1, sticky="NESW", padx=30)

# Street / Village
a_street_village = tk.Label(add_contact, text="Street / Village", font=("Arial", 12), bg="#EFF5F5")
a_street_village.grid(row=7, column=0, sticky="NESW")

a_street_village_input = tk.Entry(add_contact, font=("Arial", 12))
a_street_village_input.grid(row=7, column=1, sticky="NESW", padx=30)

# City / Municipality
a_city_municipality = tk.Label(add_contact, text="City / Municipality", font=("Arial", 12), bg="#EFF5F5")
a_city_municipality.grid(row=8, column=0, sticky="NESW")

a_city_municipality_input = tk.Entry(add_contact, font=("Arial", 12))
a_city_municipality_input.grid(row=8, column=1, sticky="NESW", padx=30)

# Province
a_province = tk.Label(add_contact, text="Province", font=("Arial", 12), bg="#EFF5F5")
a_province.grid(row=9, column=0, sticky="NESW")

a_province_input = tk.Entry(add_contact, font=("Arial", 12))
a_province_input.grid(row=9, column=1, sticky="NESW", padx=30)

# Country
a_country = tk.Label(add_contact, text="Country", font=("Arial", 12), bg="#EFF5F5")
a_country.grid(row=10, column=0, sticky="NESW")

a_country_input = tk.Entry(add_contact, font=("Arial", 12))
a_country_input.grid(row=10, column=1, sticky="NESW", padx=30)

# Back btn to main menu
a_back_btn = tk.Button(add_contact, text="Back", font=("Arial", 12), bg="#EFF5F5", command=lambda:show_frame(main_menu))
a_back_btn.grid(row=11, column=0, sticky="W", ipadx=10 ,padx=30)


# Submit btn (change function)
a_submit_btn = tk.Button(add_contact, text="Submit", font=("Arial", 12), bg="#EB6440", command=check_infos)
a_submit_btn.grid(row=11, column=1, sticky="E", ipadx=10 ,padx=30)










# Starting frame
show_frame(main_menu)
# Reprompt when closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()






# This will import all the widgets
# and modules which are available in
# tkinter and ttk module

 
 
# class NewWindow(Toplevel):
     
#     def __init__(self, master = None):
         
#         super().__init__(master = master)
#         self.title("New Window")
#         self.geometry("200x200")
#         label = Label(self, text ="This is a new Window")
#         label.pack()
 
 
# # creates a Tk() object
# master = Tk()
 
# # sets the geometry of
# # main root window
# master.geometry("200x200")
 
# label = Label(master, text ="Main Menu")
# label.pack(side = TOP, pady = 10)
 
# label = Label(master, text ="What would you like to do?", font='arial 10 bold').pack()

# # a button widget which will
# # open a new window on button click
# btn = Button(master,
#              text ="Click to open a new window")
 
# # Following line will bind click event
# # On any click left / right button
# # of mouse a new window will be opened
# btn.bind("<Button>",
#          lambda e: NewWindow(master))
 
# btn.pack(pady = 10)
 
# # mainloop, runs infinitely
# mainloop()






















# ws = Tk()
# ws.title('Python Guides')
# ws.geometry('500x400')
# ws.config(bg="#447c84")
# ws.attributes('-fullscreen',True)

# functions

# from tkinter import ttk


# class Window(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.geometry('300x100')
#         self.title('Toplevel Window')

#         ttk.Button(self,
#                 text='Close',
#                 command=self.destroy).pack(expand=True)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.geometry('720x576')
#         self.title('Main Menu')

#         tk.Label(self, text = 'Main Menu', font='arial 16 bold').pack()
#         tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = '1 - Add Contacts', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()

#         # place a button on the root window
#         ttk.Button(self,
#                 text = 'Add Contacts',
#                 command=self.open_window("add")).pack()

#         ttk.Button(self,
#                 text = 'Go',
#                 command=self.open_window).place(x="450", y="84")


#     def open_window(self, todo):
#         if todo == "add":
#             window = Window(self)
#             window.grab_set()
#         else:
#             pass




# if __name__ == "__main__":
#     app = App()
#     app.mainloop()













# def main_menu():

#     print("Main Menu\nWhat would you like  to do?")
#     print("1 - Add Contact\n2 - Edit Contact\n3 - Delete Contact\n4 - View Contacts\n5 - Search Address Book\n6 - Exit\n")
    
#     # Keep prompting the user until a valid answer is given
#     # (add counter for when user exceed 5 reask the question and give sggestions)
#     # accept string inputs like add contact or edit contact
#     options = [str(number) for number in range(1,7)]
#     while True:
#         option = input("Choose an option:  ").lstrip("0")
#         if option in options:
#             break

#     # Prompt again depending on what the user want to do
#     if option == options[0]:
#         add_contact()
    
#     elif option == options[1]:
#         edit_contact()
    
#     elif option == options[2]:
#         delete_contact()
    
#     elif option == options[3]:
#         view_contact()
    
#     elif option == options[4]:
#         search_address_book()
    
#     else:
#         sys.exit("The program is closing. Thank you!")

    
    
# def add_contact():
#     # Prompt for first name, last name, address, and contact number
#     print("\nFill up the details for the new contact")
    
#     # Get the names 
#     first_name = get_name("first_name")
#     last_name = get_name("last_name")

#     print(first_name, last_name)
#     print("successfully got the name")

#     # Get the full address

    
#     print("\nFill up the contact's full address (NA if not sure)")



#     # main_menu()






        
    

            
# def edit_contact():
#     pass

# def delete_contact():
#     pass

# def view_contact():
#     pass

# def search_address_book():
#     pass










# if __name__ == "__main__":
# 	main_menu()