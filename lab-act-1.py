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
    # Clear inputs when going back to main menu
    if frame == main_menu:
        inputs = [e_entry_no_input, e_firstname_input, e_lastname_input, e_address_input, e_number_input]
        clear_inputs(inputs)

    elif frame == edit_contact:
        # Do not redirect to edit contact frame if db is empty
        if len(db) < 1:
            if messagebox.askyesno(title="Error", message="The Address Book is currently empty.\nWould you like to add a contact?"): 
                return show_frame(add_contact)
            return

        # Hide labels and inputs when no entry number entered
        else:
            widgets_to_hide = [e_firstname, e_firstname_input, e_lastname, e_lastname_input, e_address ,e_address_input, e_number, e_number_input, e_back_btn, e_submit_btn]
            hide_widgets(widgets_to_hide)

    
        
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
    clear_inputs(inputs)

    # Inform user via message box that it is successful and redirect to main menu if no more contacts to add
    if not messagebox.askyesno(title="Success!", message=f"Successfully added {details['first name']} {details['last name']}'s contact information!\n\nWould you like to add another contact?"):
        show_frame(main_menu)    
    return



def search_db_via_entry():
    # Clear inputs
    inputs = [e_firstname_input, e_lastname_input, e_address_input, e_number_input]
    clear_inputs(inputs)

    # Get entry number
    entry_number = e_entry_no_input.get()

    # Ensure entry number is vaid
    for character in entry_number:
        if character not in digits:
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 
        entry_number = int(entry_number)
        if entry_number < 1 or entry_number > 50:
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 

    number_of_entries_in_db = len(db)
    if entry_number > number_of_entries_in_db:
            return messagebox.showerror(title="Error", message=f"The Address Book only contains {number_of_entries_in_db} entries.") 

    # Open widgets and insert their values based on entry number
    e_firstname.grid(row=5, column=0, sticky="NESW", padx=30)
    e_firstname_input.insert(0, db[entry_number - 1].get("first name"))
    e_firstname_input.grid(row=5, column=1, sticky="NESW", padx=30)

    e_lastname.grid(row=6, column=0, sticky="NESW")
    e_lastname_input.insert(0, db[entry_number - 1].get("last name"))
    e_lastname_input.grid(row=6, column=1, sticky="NESW", padx=30)
    
    e_address.grid(row=7, column=0, sticky="NESW", padx=30)
    e_address_input.insert(0, db[entry_number - 1].get("address"))
    e_address_input.grid(row=7, column=1, sticky="NESW", padx=30)

    e_number.grid(row=8, column=0, sticky="NESW")
    e_number_input.insert(0, db[entry_number - 1].get("contact number"))
    e_number_input.grid(row=8, column=1, sticky="NESW", padx=30, pady=15)

    e_back_btn.grid(row=12, column=0, sticky="W", ipadx=10, padx=30, pady=15)
    e_submit_btn.grid(row=12, column=1, sticky="E", ipadx=10, padx=30, pady=15)

    return

def hide_widgets(widgets):
    for widget in widgets:
        widget.grid_forget()

def clear_inputs(inputs):
    for input in inputs:
        input.delete(0, tk.END)

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

# JUST FOR TESTING TO NO LONGER NEED TO ADD A CONTACT
db.append({"first name": "Sieg", "last name": "Mina", "contact number": "0945160",
                        "address": "Canada"})

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
a_back_btn.grid(row=11, column=0, sticky="W", ipadx=10, padx=30, pady=15)

# Submit btn (change function)
a_submit_btn = tk.Button(add_contact, text="Submit", font=("Arial", 12), bg="#EB6440", command=check_infos)
a_submit_btn.grid(row=11, column=1, sticky="E", ipadx=10, padx=30, pady=15)


# Edit Contact (e in var stands for edit contact frame) 
# Configure the number of rows and column in add contact frame
for number in range(12):
    edit_contact.grid_rowconfigure(number, weight=1)

for number in range(2):
    edit_contact.grid_columnconfigure(number, weight=1)

# Title and description
e_title = tk.Label(edit_contact, text="Edit Contact", font=("Arial", 24), fg="white", bg="#497174")
e_title.grid(row=0, column=0, columnspan=2, sticky="NESW")

e_title = tk.Label(edit_contact, text="Enter entry number to edit.", font=("Arial", 14), bg="#EFF5F5")
e_title.grid(row=1, column=0, columnspan=2, sticky="NESW")

e_entry_no_input = tk.Entry(edit_contact, font=("Arial", 12))
e_entry_no_input.grid(row=2, column=0, sticky="E", padx=30, pady=15)

e_submit_btn = tk.Button(edit_contact, text="Search", font=("Arial", 12), bg="#EB6440", command=search_db_via_entry)
e_submit_btn.grid(row=2, column=1, sticky="W", ipadx=10, pady=15)

# Forms
# Firstname
e_firstname = tk.Label(edit_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
e_firstname.grid(row=5, column=0, sticky="NESW", padx=30)
e_firstname.grid_forget()

e_firstname_input = tk.Entry(edit_contact, font=("Arial", 12))
e_firstname_input.grid(row=5, column=1, sticky="NESW", padx=30)
e_firstname_input.grid_forget()

#Last Name
e_lastname = tk.Label(edit_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
e_lastname.grid(row=6, column=0, sticky="NESW")
e_lastname.grid_forget()

e_lastname_input = tk.Entry(edit_contact, font=("Arial", 12))
e_lastname_input.grid(row=6, column=1, sticky="NESW", padx=30)
e_lastname_input.grid_forget()

# Address
e_address = tk.Label(edit_contact, text="Address", font=("Arial", 12), bg="#EFF5F5")
e_address.grid(row=7, column=0, sticky="NESW", padx=30)
e_address.grid_forget()

e_address_input = tk.Entry(edit_contact, font=("Arial", 12))
e_address_input.grid(row=7, column=1, sticky="NESW", padx=30)
e_address_input.grid_forget()


# Contact Number
e_number = tk.Label(edit_contact, text="Contact Number", font=("Arial", 12), bg="#EFF5F5")
e_number.grid(row=8, column=0, sticky="NESW")
e_number.grid_forget()

e_number_input = tk.Entry(edit_contact, font=("Arial", 12))
e_number_input.grid(row=8, column=1, sticky="NESW", padx=30, pady=15)
e_number_input.grid_forget()


# Back btn to main menu
e_back_btn = tk.Button(edit_contact, text="Back", font=("Arial", 12), bg="#EFF5F5", command=lambda:show_frame(main_menu))
e_back_btn.grid(row=12, column=0, sticky="W", ipadx=10, padx=30, pady=15)
e_back_btn.grid_forget()

# Submit btn
e_submit_btn = tk.Button(edit_contact, text="Edit", font=("Arial", 12), bg="#EB6440", command=check_infos)
e_submit_btn.grid(row=12, column=1, sticky="E", ipadx=10, padx=30, pady=15)
e_submit_btn.grid_forget()




# Starting frame
show_frame(main_menu)
# Reprompt when closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()



# USE FOR LOOPS FOR CONFIGURING TKINTER

# CHANGE WIDTH OF ENTRY NUMBER INPUT IN EDIT

# ACTUALLY EDIT THE PAGE