"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

from string import digits, punctuation
import tkinter as tk
from tkinter import messagebox  
import re
import webbrowser


# Redirect to new frame
def show_frame(frame):
    # Clear inputs when going back to main menu
    if frame == main_menu:
        inputs = [e_entry_no_input, e_firstname_input, e_lastname_input, e_address_input, e_number_input]
        clear_inputs(inputs)
            
    elif frame == add_contact:  
        # Do not go to add contact frame if contacts is full      
        if len(db) >= MAX_CONTACTS:
            if messagebox.askyesno(title="Error", message="The Address Book is currently full.\n\nWould you like to delete a contact?"): 
                return show_frame(delete_contact)
            return show_frame(main_menu)

    elif frame in [edit_contact, delete_contact, view_contact, search_contact]:
        # Do not redirect to edit, delete, view, and search frame if there is no contact saved
        if len(db) < 1:
            if messagebox.askyesno(title="Error", message="The Address Book is currently empty.\n\nWould you like to add a contact?"): 
                return show_frame(add_contact)
            return

        # Hide labels and inputs when going to edit and delete if no entry number entered
        if frame in [edit_contact, delete_contact]:
            if frame == edit_contact: 
                widgets_to_hide = [e_firstname, e_firstname_input, e_lastname, e_lastname_input, e_address ,e_address_input, e_number, e_number_input, e_submit_btn]
            elif frame == delete_contact:
                    widgets_to_hide = [d_firstname, d_firstname_input, d_lastname, d_lastname_input, d_address ,d_address_input, d_number, d_number_input, d_submit_btn]
            hide_widgets(widgets_to_hide)

    # Go to view contact frame
    if frame == view_contact:
        view_all()
    
    # Go to search contact frame
    if frame == search_contact:
        build_search()

    # Show the frame
    return frame.tkraise()



# Check input validity then save the contact to db
def save_contact():
    # Get all information about the contact's and put in a dictionary
    details = {"first name": a_firstname_input.get(), "last name": a_lastname_input.get(), "contact number": a_number_input.get(),
                "house number": a_house_no_input.get(), "street/village": a_street_village_input.get(), 
                "city/municipality": a_city_municipality_input.get(), "province": a_province_input.get(), 
                "country": a_country_input.get()
    }

    # Ensure all details are filled up and not only filled with whitespace
    if check_if_empty(details):
        return

    # Remove unnecessary spaces in all values (starting, ending, and trailing)
    details = remove_unnecessary_spaces(details)
    
    # Check individual details for its validity
    for detail in details:
        # Check if country is valid
        if detail == "country":
            # https://gist.githubusercontent.com/mlisovyi/e8df5c907a8250e14cc1e5933ed53ffd/raw/2372fc08141c690eb866a7cfbe6e2e4ea185e9f7/countryinfo.py
            global countries
            countries=['Andorra', 'Afghanistan', 'Antigua and Barbuda', 'Albania', 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada', 'Democratic Republic of the Congo', 'Republic of the Congo', "Ivory Coast", 'Chile', 'Cameroon', "China", 'Colombia', 'Costa Rica', 'Cuba', 'Cape Verde', 'Cyprus', 'Czech Republic', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Ecuador', 'Estonia', 'Egypt', 'Eritrea', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Gabon', 'Georgia', 'Ghana', 'The Gambia', 'Guinea', 'Greece', 'Guatemala', 'Haiti', 'Guinea-Bissau', 'Guyana', 'Honduras', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq', 'Iran', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Kiribati', 'North Korea', 'South Korea', 'Kuwait', 'Lebanon', 'Liechtenstein', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Madagascar', 'Marshall Islands', 'Macedonia', 'Mali', 'Myanmar', 'Mongolia', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sudan', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Somalia', 'Suriname', 'SÃ£o TomÃ© and PrÃ\xadncipe', 'Syria', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago', 'Tuvalu', 'Tanzania', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Uzbekistan', 'Vatican City', 'Venezuela', 'Vietnam', 'Vanuatu', 'Yemen', 'Zambia', 'Zimbabwe', 'Algeria', 'Bosnia and Herzegovina', 'Cambodia', 'Central African Republic', 'Chad', 'Comoros', 'Croatia', 'East Timor', 'El Salvador', 'Equatorial Guinea', 'Grenada', 'Kazakhstan', 'Laos', 'Federated States of Micronesia', 'Moldova', 'Monaco', 'Montenegro', 'Morocco', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Serbia', 'South Africa', 'Spain', 'Sri Lanka', 'Swaziland', 'Switzerland', 'United Arab Emirates', 'United Kingdom', 'Taiwan', 'Hong Kong', 'Kosovo', 'Puerto Rico']
            countries = [country.upper() for country in countries]

            # Ask if user input wrong, ask want to see all available country
            if details.get(detail).upper() not in countries:
                if messagebox.askyesno(title="Error", message=f"{details.get(detail).upper()} is NOT a valid country.\n\nWould you like to go and see a list of all the countries?"): 
                    webbrowser.open_new_tab("https://gist.githubusercontent.com/mlisovyi/e8df5c907a8250e14cc1e5933ed53ffd/raw/2372fc08141c690eb866a7cfbe6e2e4ea185e9f7/countryinfo.py")
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
                if character not in digits and character not in "()-/+ ":
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

    # Add the compressed address to details
    details["address"] = address
    
    # Capitalize all details for uniformity
    details = capitalize_details(details)
    
    # Check if person already save by looking if a contact has exactly same first name, last name and contact number
    if in_db(details):
        return

    # Add contact into db
    db.append(details)

    # Ask to delete if contacts if full
    if len(db) >= MAX_CONTACTS:
        if messagebox.askyesno(title="Error", message="The Address Book is currently full.\n\nWould you like to delete a contact?"): 
            return show_frame(delete_contact)
        return show_frame(main_menu)

    # Inform user via message box that it is successful and redirect to main menu if no more contacts to add
    if not messagebox.askyesno(title="Success!", message=f"Successfully added {details['first name']} {details['last name']}'s contact information!\n\nWould you like to add another contact?"):
        show_frame(main_menu)    

    # Clear inputs
    inputs = [a_firstname_input, a_lastname_input, a_number_input, a_house_no_input, a_street_village_input, a_city_municipality_input, a_province_input, a_country_input]
    return clear_inputs(inputs)



# Search contact via entry (called in edit contact and delete contact frame)
def search_db_via_entry(current_frame):
    # Determine which widgets to used based on current frame
    if current_frame == edit_contact:
        widgets_to_hide = [e_firstname, e_firstname_input, e_lastname, e_lastname_input, e_address ,e_address_input, e_number, e_number_input, e_submit_btn]
        inputs = [e_firstname_input, e_lastname_input, e_address_input, e_number_input]
    elif current_frame == delete_contact:
        widgets_to_hide = [d_firstname, d_firstname_input, d_lastname, d_lastname_input, d_address ,d_address_input, d_number, d_number_input, d_submit_btn]
        inputs = [d_firstname_input, d_lastname_input, d_address_input, d_number_input]
        
        # Enable inputs
        enable_inputs(inputs)

    # Clear inputs
    clear_inputs(inputs)

    # Get entry number
    global entry_number
    if current_frame == edit_contact:
        entry_number = e_entry_no_input.get()
    elif current_frame == delete_contact:
        entry_number = d_entry_no_input.get()

    # Ensure entry number is not empty
    if not entry_number:
        # Clear and hide widgets
        clear_inputs(inputs)
        hide_widgets(widgets_to_hide)
        return messagebox.showerror(title="Error", message="Enter entry numbers to edit.") 

    # Ensure entry number is valid
    for character in entry_number:
        if character.isspace():
            # Clear and hide widgets
            clear_inputs(inputs)
            hide_widgets(widgets_to_hide)
            return messagebox.showerror(title="Error", message="Avoid using whitespaces.") 

        if character not in digits:
            # Clear and hide widgets
            clear_inputs(inputs)
            hide_widgets(widgets_to_hide)
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 
       
       # Change entry number from string to int
        entry_number = int(entry_number)

        if entry_number < 1 or entry_number > MAX_CONTACTS:
            # Clear and hide widgets
            clear_inputs(inputs)
            hide_widgets(widgets_to_hide)
            return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 

    # Check if a contact actually has that entry number
    number_of_entries_in_db = len(db)
    if entry_number > number_of_entries_in_db:
            # Clear and hide widgets
            clear_inputs(inputs)
            hide_widgets(widgets_to_hide)
            return messagebox.showerror(title="Error", message=f"The Address Book only contains {number_of_entries_in_db} entries.") 

    # Open widgets and insert their values based on entry number   
    if current_frame == edit_contact: 
        e_firstname.grid(row=5, column=0, sticky="NESW", padx=10)
        e_firstname_input.insert(0, db[entry_number - 1].get("first name"))
        e_firstname_input.grid(row=5, column=1, sticky="NESW", padx=(0, 30))

        e_lastname.grid(row=6, column=0, sticky="NESW", padx=10)
        e_lastname_input.insert(0, db[entry_number - 1].get("last name"))
        e_lastname_input.grid(row=6, column=1, sticky="NESW", padx=(0, 30))
        
        e_address.grid(row=7, column=0, sticky="NESW", padx=10)
        e_address_input.insert(0, db[entry_number - 1].get("address"))
        e_address_input.grid(row=7, column=1, sticky="NESW", padx=(0, 30))

        e_number.grid(row=8, column=0, sticky="NESW", padx=10)
        e_number_input.insert(0, db[entry_number - 1].get("contact number"))
        e_number_input.grid(row=8, column=1, sticky="NESW", padx=(0, 30))

        e_submit_btn.grid(row=11, column=1, sticky="E", ipadx=10, padx=30, pady=15)

    elif current_frame == delete_contact:
        d_firstname.grid(row=5, column=0, sticky="NESW", padx=10)
        d_firstname_input.insert(0, db[entry_number - 1].get("first name"))
        d_firstname_input.grid(row=5, column=1, sticky="NESW", padx=(0, 30))
        
        d_lastname.grid(row=6, column=0, sticky="NESW")
        d_lastname_input.insert(0, db[entry_number - 1].get("last name"))
        d_lastname_input.grid(row=6, column=1, sticky="NESW", padx=(0, 30))

        d_address.grid(row=7, column=0, sticky="NESW", padx=10)
        d_address_input.insert(0, db[entry_number - 1].get("address"))
        d_address_input.grid(row=7, column=1, sticky="NESW", padx=(0, 30))

        d_number.grid(row=8, column=0, sticky="NESW")
        d_number_input.insert(0, db[entry_number - 1].get("contact number"))
        d_number_input.grid(row=8, column=1, sticky="NESW",padx=(0, 30))

        d_submit_btn.grid(row=11, column=1, sticky="E", ipadx=10, padx=30, pady=15)

        # Disable inputs when in delete frame (because delete frame only delete contact not edit)
        disable_inputs(inputs)
    return



# Check edits in edit contact frame then save those edits 
def save_edit():
    details = {"first name": e_firstname_input.get(), "last name": e_lastname_input.get(),
                "address": e_address_input.get(), "contact number": e_number_input.get()
    }

    # Ensure all details are filled up and not only filled with whitespace
    if check_if_empty(details):
        return

    # Remove unnecessary spaces in all values (starting, ending, and trailing)
    details = remove_unnecessary_spaces(details)

    # Check if input details is valid
    for detail in details:
        # Check if names is valid
        if detail in ["first name", "last name"]:
            for character in details.get(detail):
                if character in digits or character in punctuation:
                    return messagebox.showerror(title="Error", message=f"{detail.upper()} must NOT contain numbers or punctuations.") 

        # Ensure contact number has only number and some special charachters
        elif detail == "contact number":
            for character in details.get(detail):
                if character not in digits and character not in "()-/+ ":
                    return messagebox.showerror(title="Error", message=f"{detail.upper()} must only contain digits.")     

    # Capitalize all details for uniformity
    details = capitalize_details(details)

    # Ensure an edit is made
    if details["first name"] == db[entry_number - 1].get("first name") and details["last name"] == db[entry_number - 1].get("last name") and details["address"] == db[entry_number - 1].get("address") and details["contact number"] == db[entry_number - 1].get("contact number"):
        return messagebox.showerror(title="Error", message="No changes were made.")     

    # Save the edit by changing the one in db based on the entry number
    keys = ["first name", "last name", "address", "contact number"]
    for key in keys:
        db[entry_number - 1][key] = details.get(key)

    # Inform user via message box that it is successful and redirect to main menu if no more contacts to edit
    if not messagebox.askyesno(title="Success!", message=f"Successfully edited {details['first name']} {details['last name']}'s contact information!\n\nWould you like to edit another contact?"):
        show_frame(main_menu)    

    # Clear and hide widgets for the new contact to edit
    inputs = [e_entry_no_input, e_firstname_input, e_lastname_input, e_address_input, e_number_input]
    widgets_to_hide = [e_firstname, e_firstname_input, e_lastname, e_lastname_input, e_address ,e_address_input, e_number, e_number_input, e_submit_btn]
    clear_inputs(inputs)
    hide_widgets(widgets_to_hide)
    return



# Reask the user if sure to delete
def delete():
    if messagebox.askyesno(title="Delete?", message=f"Are you sure you want to delete {db[entry_number - 1].get('first name')} {db[entry_number - 1].get('last name')} in your contact?"):
        db.pop(entry_number - 1)
        show_frame(main_menu)
    return



# Load the all widgets in view contact frame
def view_all():
    # Clear the view contact widget    
    for widget in view_contact.winfo_children():
        widget.destroy()

    # Configure the number of rows and columns for view contact frame (based on number of entries in db)
    no_rows = len(db) + 20
    for number in range(no_rows):
        view_contact.grid_rowconfigure(number, weight=1)

    for number in range(5):
        view_contact.grid_columnconfigure(number, weight=1)

    # Show all contacts' information
    for count, contact in enumerate(db, 1):
        tk.Label(view_contact, text=count, font=("Arial", 12), bg="#EFF5F5").grid(row=count + 3, column=0, sticky="NESW")
        tk.Label(view_contact, text=contact.get("first name"), font=("Arial", 12), bg="#EFF5F5").grid(row=count + 3, column=1, sticky="NESW")
        tk.Label(view_contact, text=contact.get("last name"), font=("Arial", 12), bg="#EFF5F5").grid(row=count + 3, column=2, sticky="NESW")
        tk.Label(view_contact, text=contact.get("contact number"), font=("Arial", 12), bg="#EFF5F5").grid(row=count + 3, column=3, sticky="NESW")
        tk.Label(view_contact, text=contact.get("address"), font=("Arial", 12), bg="#EFF5F5").grid(row=count + 3, column=4, sticky="NESW")

    # View Contact (v in var stands for view contact frame) 
    # Title and description
    v_title = tk.Label(view_contact, text="View Contacts", font=("Arial", 24), fg="white", bg="#497174")
    v_title.grid(row=0, column=0, columnspan=5, sticky="NESW")

    v_description = tk.Label(view_contact, text="All contacts in Address Book.", font=("Arial", 14), bg="#EFF5F5")
    v_description.grid(row=1, column=0, columnspan=5, sticky="NESW")

    v_entry_number = tk.Label(view_contact, text="Entry No.", font=("Arial", 14), bg="#EFF5F5")
    v_entry_number.grid(row=2, column=0, sticky="NESW")

    v_firstname = tk.Label(view_contact, text="First Name", font=("Arial", 14), bg="#EFF5F5")
    v_firstname.grid(row=2, column=1, sticky="NESW")

    v_lastname = tk.Label(view_contact, text="Last Name", font=("Arial", 14), bg="#EFF5F5")
    v_lastname.grid(row=2, column=2, sticky="NESW")

    v_number = tk.Label(view_contact, text="Number", font=("Arial", 14), bg="#EFF5F5")
    v_number.grid(row=2, column=3, sticky="NESW")

    v_address = tk.Label(view_contact, text="Address", font=("Arial", 14), bg="#EFF5F5")
    v_address.grid(row=2, column=4, sticky="NESW")

    v_back_btn = tk.Button(view_contact, text="Back",bg="#EB6440" ,command=lambda:show_frame(main_menu))
    v_back_btn.grid(row=no_rows, column=0, sticky="W",ipadx=10, padx=30, pady=15)

    # Full screen to better view the contacts since some informations can be lengthy
    return root.state("zoomed") 



# Load the widgets needed to ask what to search
def build_search():
    # Clear the search contact widget    
    for widget in search_contact.winfo_children():
        widget.destroy()

    # Search Contact (s in var stands for search contact frame) 
    # Configure the number of rows and columns initially for search contact frame
    for number in range(55):
        search_contact.grid_rowconfigure(number, weight=1)

    for number in range(5):
        search_contact.grid_columnconfigure(number, weight=1)

    # Title and description
    s_title = tk.Label(search_contact, text="Search Contact", font=("Arial", 24), fg="white", bg="#497174")
    s_title.grid(row=0, column=0, columnspan=5, sticky="NESW")

    s_description = tk.Label(search_contact, text="Search by any of the following.\n(leave blank to ignore)", font=("Arial", 14), bg="#EFF5F5")
    s_description.grid(row=1, column=0, columnspan=5, sticky="NESW")
   
    # Column title
    s_entry_no = tk.Label(search_contact, text="Entry No.", font=("Arial", 14), bg="#EFF5F5")
    s_entry_no.grid(row=2, column=0, sticky="NESW")

    s_firstname = tk.Label(search_contact, text="First Name", font=("Arial", 14), bg="#EFF5F5")
    s_firstname.grid(row=2, column=1, sticky="NESW")
   
    s_lastname = tk.Label(search_contact, text="Last Name", font=("Arial", 14), bg="#EFF5F5")
    s_lastname.grid(row=2, column=2, sticky="NESW")

    s_number = tk.Label(search_contact, text="Contact Number", font=("Arial", 14), bg="#EFF5F5")
    s_number.grid(row=2, column=3, sticky="NESW")

    s_address = tk.Label(search_contact, text="Address", font=("Arial", 14), bg="#EFF5F5")
    s_address.grid(row=2, column=4, sticky="NESW")

    # Inputs
    s_entry_no_input = tk.Entry(search_contact, font=("Arial", 12))
    s_entry_no_input.grid(row=3, column=0, sticky="NESW", padx=30, pady=15)

    s_firstname_input = tk.Entry(search_contact, font=("Arial", 12))
    s_firstname_input.grid(row=3, column=1, sticky="NESW", padx=30, pady=15)

    s_lastname_input = tk.Entry(search_contact, font=("Arial", 12))
    s_lastname_input.grid(row=3, column=2, sticky="NESW", padx=30, pady=15)

    s_number_input = tk.Entry(search_contact, font=("Arial", 12))
    s_number_input.grid(row=3, column=3, sticky="NESW", padx=30, pady=15)

    s_address_input = tk.Entry(search_contact, font=("Arial", 12))
    s_address_input.grid(row=3, column=4, sticky="NESW", padx=30, pady=15)
    
    # Search btn
    s_search_btn = tk.Button(search_contact, text="Search", font=("Arial", 12), bg="#EB6440" ,command=lambda:search_match(s_entry_no_input.get(), s_firstname_input.get(), s_lastname_input.get(), s_number_input.get(), s_address_input.get()))
    s_search_btn.grid(row=4, column=2, sticky="NESW", ipadx=10, padx=30, pady=15)  

    # Back btn to main menu
    s_back_btn = tk.Button(search_contact, text="Back",bg="#EB6440" ,command=lambda:show_frame(main_menu))
    s_back_btn.grid(row=55, column=0, sticky="W",ipadx=10, padx=30, pady=15)

    # Full screen to better view the contacts since some informations can be lengthy
    return root.state("zoomed") 



# Check inputs, find matches based on query, and load matching contacts
def search_match(entry_no, firstname, lastname, number, address):
    details = [entry_no, firstname, lastname, number, address]
    matches = []
    
    # Clear results and rebuild the top part
    build_search()

    # Ensure an information is entered
    if entry_no.isspace() and firstname.isspace() and lastname.isspace() and number.isspace() and address.isspace():
        return messagebox.showerror(title="Error", message="Enter information to search.") 
    if not entry_no and not firstname and not lastname and not number and not address:
        return messagebox.showerror(title="Error", message="Enter detail(s) to search.") 

    # Check if details are correct
    for detail in details:
        if detail == entry_no:
            if entry_no:
                # Check if entry is valid
                for character in entry_no:
                    if character.isspace():
                        return messagebox.showerror(title="Error", message="Avoid using whitespaces in ENTRY NO.") 

                    if character not in digits:
                        return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 
        
                # Change entry number from string to int
                entry_no = int(entry_no)

                # Check if entry number is within 1-50
                if entry_no < 1 or entry_no > MAX_CONTACTS:
                    return messagebox.showerror(title="Error", message="Entry numbers can only be be 1-50 inclusive.") 
                
                # Check if entry number matches an exisiting contact
                number_of_entries_in_db = len(db)
                if entry_no > number_of_entries_in_db:
                        return messagebox.showerror(title="Error", message="No matches.\n(entry no. doesn't exist)") 

                # Include the contact matching the entry number to matches list
                matches.append((entry_no, db[entry_no - 1]))
        
        if detail == firstname:
            if firstname:
                # Remove unnecessary whitespaces and capitalize
                firstname = re.sub(' +', ' ',firstname.strip()).upper()

                # Check if first name is valid
                for character in firstname:
                    if character in digits or character in punctuation:
                        return messagebox.showerror(title="Error", message=f"FIRST NAME must NOT contain numbers or punctuations.") 

                # Check all contact if there is a match
                for count, contact in enumerate(db, 1):
                    if firstname == contact.get("first name"):
                        matches.append((count, contact))   
                
                # Show error if no matches
                if len(matches) == 0:
                    return messagebox.showerror(title="Error", message=f"No matches.\n(No contact has a first name of '{firstname}'.)") 

        if detail == lastname:
            if lastname:
                # Remove unnecessary whitespaces and capitalize
                lastname = re.sub(' +', ' ',lastname.strip()).upper()

                # Check if last name is valid
                for character in lastname:
                    if character in digits or character in punctuation:
                        return messagebox.showerror(title="Error", message=f"LAST NAME must NOT contain numbers or punctuations.") 

                # Check all contact if there is a match
                for count, contact in enumerate(db, 1):
                    if lastname == contact.get("last name"):
                        matches.append((count, contact))   

                # Show error if no matches
                if len(matches) == 0:
                    return messagebox.showerror(title="Error", message=f"No matches.\n(No contact has a last name of '{lastname}'.)") 

        if detail == number:
            if number:
                # Remove unnecessary whitespaces
                number = re.sub(' +', ' ',number.strip())

                # Check if number is valid
                for character in number:
                    if character not in digits and character not in "()-/+ ":
                        return messagebox.showerror(title="Error", message="CONTACT NUMBER must only contain digits.") 

                # Check all contact if there is a match
                for count, contact in enumerate(db, 1):
                    if number == contact.get("contact number"):
                        matches.append((count, contact))   

                # Show error if no matches
                if len(matches) == 0:
                    return messagebox.showerror(title="Error", message=f"No matches.\n(No contact has a contact number of '{number}'.)") 

        if detail == address:
            if address:
                # Remove unnecessary whitespaces and capitalize
                address = re.sub(' +', ' ',address.strip()).upper()

                # Check all contact if there is a match
                for count, contact in enumerate(db, 1):
                    if address == contact.get("address"):
                        matches.append((count, contact))

                # Show error if no matches
                if len(matches) == 0:
                    return messagebox.showerror(title="Error", message=f"No matches.\n(No contact has a address of '{address}'.)") 

        # Show all contacts that matches the details user inputted
        if len(matches) > 0:
            for row, (count, contact) in enumerate(matches):
                tk.Label(search_contact, text=count, font=("Arial", 12), bg="#EFF5F5").grid(row=row + 5, column=0, sticky="NESW")
                tk.Label(search_contact, text=contact.get("first name"), font=("Arial", 12), bg="#EFF5F5").grid(row=row + 5, column=1, sticky="NESW")
                tk.Label(search_contact, text=contact.get("last name"), font=("Arial", 12), bg="#EFF5F5").grid(row=row + 5, column=2, sticky="NESW")
                tk.Label(search_contact, text=contact.get("contact number"), font=("Arial", 12), bg="#EFF5F5").grid(row=row + 5, column=3, sticky="NESW")
                tk.Label(search_contact, text=contact.get("address"), font=("Arial", 12), bg="#EFF5F5").grid(row=row + 5, column=4, sticky="NESW")



def remove_unnecessary_spaces(details):
    for detail in details:
        details[detail] = re.sub(' +', ' ',details.get(detail).strip())
    return details

def capitalize_details(details):
    for detail in details:
        details[detail] = details.get(detail).upper()
    return details


def check_if_empty(details):
    for detail in details:
        if not details.get(detail) or details.get(detail).isspace():
            messagebox.showerror(title="Error", message="Details are incomplete. Please fill up all the details.") 
            return True
    else:
        return False

def in_db(details):
    for entry in db:
            if entry["first name"] == details["first name"] and entry["last name"] == details["last name"] and entry["contact number"] == details["contact number"]:
                messagebox.showerror(title="Error", message=f"{details['first name'].upper()} {details['last name'].upper()}'s contact information is already saved.") 
                return True
    else:
        return False

def disable_inputs(inputs):
    for input in inputs:
        input.configure(state="disabled")

def delete_widget(widgets):  
    for widget in widgets:
        widget.destory()    

def enable_inputs(inputs):
    for input in inputs:
        input.configure(state="normal")

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

if __name__ == "__main__":
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

    # Address Book db where all contacts is saved
    db = []
    MAX_CONTACTS = 50

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

    add_contact.grid_columnconfigure(0, weight=1)
    add_contact.grid_columnconfigure(1, weight=50)

    # Title and description 
    a_title = tk.Label(add_contact, text="Add Contact", font=("Arial", 24), fg="white", bg="#497174")
    a_title.grid(row=0, column=0, columnspan=2, sticky="NESW", pady=5)

    a_description = tk.Label(add_contact, text="Fill up the new contact's details.", font=("Arial", 18), bg="#EFF5F5")
    a_description.grid(row=1, column=0, columnspan=2, sticky="NESW", pady=5)

    # Forms

    a_firstname = tk.Label(add_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
    a_firstname.grid(row=2, column=0, sticky="E", padx=10)

    a_firstname_input = tk.Entry(add_contact, font=("Arial", 12))
    a_firstname_input.grid(row=2, column=1, sticky="NESW", padx=(0, 30))

    #Last Name
    a_lastname = tk.Label(add_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
    a_lastname.grid(row=3, column=0, sticky="E", padx=10)

    a_lastname_input = tk.Entry(add_contact, font=("Arial", 12))
    a_lastname_input.grid(row=3, column=1, sticky="NESW", padx=(0, 30))

    # Contact Number
    a_number = tk.Label(add_contact, text="Contact Number", font=("Arial", 12), bg="#EFF5F5")
    a_number.grid(row=4, column=0, sticky="E", padx=10)

    a_number_input = tk.Entry(add_contact, font=("Arial", 12))
    a_number_input.grid(row=4, column=1, sticky="NESW", padx=(0, 30), pady=15)

    # Address
    a_address = tk.Label(add_contact, text="Address", font=("Arial", 16), bg="#EFF5F5")
    a_address.grid(row=5, column=0, sticky="E", ipadx=10, padx=20)

    # House Number
    a_house_no = tk.Label(add_contact, text="House Number", font=("Arial", 12), bg="#EFF5F5")
    a_house_no.grid(row=6, column=0, sticky="E", padx=10)

    a_house_no_input = tk.Entry(add_contact, font=("Arial", 12))
    a_house_no_input.grid(row=6, column=1, sticky="NESW", padx=(0, 30))

    # Street / Village
    a_street_village = tk.Label(add_contact, text="Street / Village", font=("Arial", 12), bg="#EFF5F5")
    a_street_village.grid(row=7, column=0, sticky="E", padx=10)

    a_street_village_input = tk.Entry(add_contact, font=("Arial", 12))
    a_street_village_input.grid(row=7, column=1, sticky="NESW", padx=(0, 30))

    # City / Municipality
    a_city_municipality = tk.Label(add_contact, text="City / Municipality", font=("Arial", 12), bg="#EFF5F5")
    a_city_municipality.grid(row=8, column=0, sticky="E", padx=10)

    a_city_municipality_input = tk.Entry(add_contact, font=("Arial", 12))
    a_city_municipality_input.grid(row=8, column=1, sticky="NESW", padx=(0, 30))

    # Province
    a_province = tk.Label(add_contact, text="Province", font=("Arial", 12), bg="#EFF5F5")
    a_province.grid(row=9, column=0, sticky="E", padx=10)

    a_province_input = tk.Entry(add_contact, font=("Arial", 12))
    a_province_input.grid(row=9, column=1, sticky="NESW",padx=(0, 30))

    # Country
    a_country = tk.Label(add_contact, text="Country", font=("Arial", 12), bg="#EFF5F5")
    a_country.grid(row=10, column=0, sticky="E",padx=10)

    a_country_input = tk.Entry(add_contact, font=("Arial", 12))
    a_country_input.grid(row=10, column=1, sticky="NESW", padx=(0, 30))

    # Back btn to main menu
    a_back_btn = tk.Button(add_contact, text="Back", font=("Arial", 12), bg="#EFF5F5", command=lambda:show_frame(main_menu))
    a_back_btn.grid(row=11, column=0, sticky="W", ipadx=10, padx=30, pady=15)

    # Submit btn
    a_submit_btn = tk.Button(add_contact, text="Submit", font=("Arial", 12), bg="#EB6440", command=save_contact)
    a_submit_btn.grid(row=11, column=1, sticky="E", ipadx=10, padx=30, pady=15)



    # Edit Contact (e in var stands for edit contact frame) 
    # Configure the number of rows and column in edit contact frame
    for number in range(12):
        edit_contact.grid_rowconfigure(number, weight=1)

    for number in range(2):
        edit_contact.grid_columnconfigure(number, weight=1)

    # Title and description
    e_title = tk.Label(edit_contact, text="Edit Contact", font=("Arial", 24), fg="white", bg="#497174")
    e_title.grid(row=0, column=0, columnspan=2, sticky="NESW")

    e_description = tk.Label(edit_contact, text="Enter entry number to edit.", font=("Arial", 14), bg="#EFF5F5")
    e_description.grid(row=1, column=0, columnspan=2, sticky="NESW")

    # Entry number
    e_entry_no_input = tk.Entry(edit_contact, font=("Arial", 12))
    e_entry_no_input.grid(row=2, column=0, sticky="E", padx=30, pady=15)

    e_submit_entry_btn = tk.Button(edit_contact, text="Search", font=("Arial", 12), bg="#EB6440", command=lambda:search_db_via_entry(edit_contact))
    e_submit_entry_btn.grid(row=2, column=1, sticky="W", ipadx=10, pady=15)

    # Forms
    # Firstname
    e_firstname = tk.Label(edit_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
    e_firstname_input = tk.Entry(edit_contact, font=("Arial", 12))

    #Last Name
    e_lastname = tk.Label(edit_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
    e_lastname_input = tk.Entry(edit_contact, font=("Arial", 12))

    # Address
    e_address = tk.Label(edit_contact, text="Address", font=("Arial", 12), bg="#EFF5F5")
    e_address_input = tk.Entry(edit_contact, font=("Arial", 12))

    # Contact Number
    e_number = tk.Label(edit_contact, text="Contact Number", font=("Arial", 12), bg="#EFF5F5")
    e_number_input = tk.Entry(edit_contact, font=("Arial", 12))

    # Back btn to main menu
    e_back_btn = tk.Button(edit_contact, text="Back", font=("Arial", 12), bg="#EFF5F5", command=lambda:show_frame(main_menu))
    e_back_btn.grid(row=11, column=0, sticky="W", ipadx=10, padx=30, pady=15)

    # Submit btn
    e_submit_btn = tk.Button(edit_contact, text="Edit", font=("Arial", 12), bg="#EB6440", command=save_edit)



    # Delete Contact (d in var stands for delete contact frame) 
    # Configure the number of rows and column in delete contact frame
    for number in range(12):
        delete_contact.grid_rowconfigure(number, weight=1)

    for number in range(2):
        delete_contact.grid_columnconfigure(number, weight=1)

    # Title and description
    d_title = tk.Label(delete_contact, text="Delete Contact", font=("Arial", 24), fg="white", bg="#497174")
    d_title.grid(row=0, column=0, columnspan=2, sticky="NESW")

    d_description = tk.Label(delete_contact, text="Enter entry number to delete.", font=("Arial", 14), bg="#EFF5F5")
    d_description.grid(row=1, column=0, columnspan=2, sticky="NESW")

    # Entry number 
    d_entry_no_input = tk.Entry(delete_contact, font=("Arial", 12))
    d_entry_no_input.grid(row=2, column=0, sticky="E", padx=30, pady=15)

    d_submit_entry_btn_btn = tk.Button(delete_contact, text="Search", font=("Arial", 12), bg="#EB6440", command=lambda:search_db_via_entry(delete_contact))
    d_submit_entry_btn_btn.grid(row=2, column=1, sticky="W", ipadx=10, pady=15)

    # Details
    # Firstname
    d_firstname = tk.Label(delete_contact, text="First Name", font=("Arial", 12), bg="#EFF5F5")
    d_firstname_input = tk.Entry(delete_contact, font=("Arial", 12))

    #Last Name
    d_lastname = tk.Label(delete_contact, text="Last Name", font=("Arial", 12), bg="#EFF5F5")
    d_lastname_input = tk.Entry(delete_contact, font=("Arial", 12))

    # Address
    d_address = tk.Label(delete_contact, text="Address", font=("Arial", 12), bg="#EFF5F5")
    d_address_input = tk.Entry(delete_contact, font=("Arial", 12))

    # Contact Number
    d_number = tk.Label(delete_contact, text="Contact Number", font=("Arial", 12), bg="#EFF5F5")
    d_number_input = tk.Entry(delete_contact, font=("Arial", 12))

    # Back btn to main menu
    d_back_btn = tk.Button(delete_contact, text="Back", font=("Arial", 12), bg="#EFF5F5", command=lambda:show_frame(main_menu))
    d_back_btn.grid(row=11, column=0, sticky="W", ipadx=10, padx=30, pady=15)

    # Submit btn
    d_submit_btn = tk.Button(delete_contact, text="Delete", font=("Arial", 12), bg="#EB6440", command=delete)



    # Starting frame
    show_frame(main_menu)

    # Reprompt when closing
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()