"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

import cs50
import sys
from string import digits, punctuation
import tkinter as tk
from tkinter import messagebox  
import re
import webbrowser


from helpers import remove_unnecessary_space
# from helpers import get_name, get_house_number, get_street_vilage, get_city_municipality, get_province, get_country


# Redirect to new frame
def show_frame(frame):
    print(db)
    # Do not redirect to edit contact frame if db is empty
    if frame == edit_contact:
        if len(db) < 1:
            if messagebox.askyesno(title="Error", message="The Address Book is currently empty.\nWould you like to add a contact?"): 
                return show_frame(add_contact)
            else:
                return
    return frame.tkraise()

# Check information about contact's details
def check_infos():
    # Get all information about the contact's and put in a dictionary
    details = {"first name": a_firstname_input.get(), "last name": a_lastname_input.get(), "contact number": a_number_input.get(),
                            "house number": a_house_no_input.get(), "street/village": a_street_village_input.get(), 
                            "city/municipality": a_city_municipality_input.get(), "province": a_province_input.get(), 
                            "country": a_country_input.get()
    }

    # Ensure inputs are valid
    # Ensure all details are filled up and not only filled with whitespace
    for detail in details:
        if not details.get(detail) or details.get(detail).isspace():
            return messagebox.showerror(title="Error", message="Details are incomplete. Please fill up all the details.") 

    # Remove unnecessary spaces in all values (starting, ending, and trailing)
    for detail in details:
        details[detail] = re.sub(' +', ' ',details.get(detail).strip())
    
    # Check individual details for its validity
    for detail in details:
        # Check if country is valid
        if detail == "country":
            # https://pytutorial.com/python-country-list
            # TODO FIX THE NAMES OF SOME COUNTRIES
            countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
            countries = [country.upper() for country in countries]

            if details.get(detail).upper() not in countries:
                if messagebox.askyesno(title="Error", message=f"{details.get(detail).upper()} is NOT a valid country.\n\nGo to python-country-list to see the all countries.\nWould you like to go?"): 
                    return webbrowser.open_new_tab("https://pytutorial.com/python-country-list")
                else:
                    return

        # Ensure names, municipality, and province do not have digits and punctuations
        elif detail in ["first name", "last name", "city/municipality", "province"]:
            for character in details.get(detail):
                if character in digits or character in punctuation:
                    return messagebox.showerror(title="Error", message=f"{detail.upper()} must NOT contain numbers or punctuations.") 

        # Ensure house number only contains number
        elif detail == "house number":
            for character in details.get(detail):
                if character not in digits:
                    return messagebox.showerror(title="Error", message=f"{detail.upper()} must only contain digits.")      

        # Ensure contact number has only number and some special charachters
        elif detail == "contact number":
            for character in details.get(detail):
                if character not in digits and character not in "()-/+":
                    return messagebox.showerror(title="Error", message=f"{detail.upper()} must only contain digits.") 

    # Compress the address into a single element
    address = ""
    for detail in ["house number", "street/village", "city/municipality", "province", "country"]:
        if detail == "house number":
            address += f"{details.get(detail)} "
        elif detail == "country":
            address += details.get(detail)
        else:
            address += f"{details.get(detail)}, "

        # Delete the address' previous elements
        details.pop(detail)

    details["address"] = address
    
    # Capitalize all details for uniformity
    for detail in details:
        details[detail] = details.get(detail).upper()
    
    # Ensure person is not already in db
    for entry in db:
        if entry["first name"] == details["first name"] and entry["last name"] == details["last name"] and entry["contact number"] == details["contact number"]:
            return messagebox.showerror(title="Error", message=f"{details['first name'].upper()} {details['last name'].upper()}'s contact information is already saved.") 


    # Add contact into db
    db.append(details)

    # Clear inputs (aka entries)
    inputs = [a_firstname_input, a_lastname_input, a_number_input, a_house_no_input, a_street_village_input, a_city_municipality_input, a_province_input, a_country_input]
    for input in inputs:
        input.delete(0, tk.END)

    # Inform user via message box that it is successful and redirect to main menu if no more contacts to add
    if not messagebox.askyesno(title="Success!", message=f"Successfully added {details['first name']} {details['last name']}'s contact information!\n\nWould you like to add another contact?"):
        show_frame(main_menu)    
    return



def search_db_via_entry():
    entry_number = e_entry_no_input.get()

    for character in entry_number:
        if character not in digits:
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 
        entry_number = int(entry_number)
        if entry_number < 1 or entry_number > 50:
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 

    number_of_entries_in_db = len(db)
    if entry_number > number_of_entries_in_db:
            return messagebox.showerror(title="Error", message=f"The Address Book only have {number_of_entries_in_db}") 

    print(number_of_entries_in_db)
    print(entry_number)



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

# Address Book db
db = []

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
    add_contact.grid_columnconfigure(number, weight=1)

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




# Edit Contact (e in var stands for edit contact frame) 
# Configure the number of rows and column in add contact frame
for number in range(13):
    edit_contact.grid_rowconfigure(number, weight=1)

for number in range(2):
    edit_contact.grid_columnconfigure(number, weight=1)

# Title and description
e_title = tk.Label(edit_contact, text="Edit Contact", font=("Arial", 24), fg="white", bg="#497174")
e_title.grid(row=0, column=0, columnspan=2, sticky="NESW")

e_title = tk.Label(edit_contact, text="Enter entry number to search.", font=("Arial", 14), bg="#EFF5F5")
e_title.grid(row=1, column=0, columnspan=2, sticky="NESW")

e_entry_no_input = tk.Entry(edit_contact, text="First Name", font=("Arial", 12))
e_entry_no_input.grid(row=2, column=0, sticky="E", padx=30)

e_submit_btn = tk.Button(edit_contact, text="Submit", font=("Arial", 12), bg="#EB6440", command=search_db_via_entry)
e_submit_btn.grid(row=2, column=1, sticky="W", ipadx=10)

# # Forms
# # Firstname
# e_firstname = tk.Label(edit_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
# e_firstname.grid(row=3, column=0, sticky="NESW", padx=30)

# e_firstname_input = tk.Entry(edit_contact, font=("Arial", 12))
# e_firstname_input.grid(row=3, column=1, sticky="NESW", padx=30)

# #Last Name
# a_lastname = tk.Label(edit_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
# a_lastname.grid(row=4, column=0, sticky="NESW")









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