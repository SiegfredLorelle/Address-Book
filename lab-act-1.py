"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

import cs50
import sys

from helpers import get_name

def main_menu():
    print("Main Menu\nWhat would you like  to do?")
    print("1 - Add Contact\n2 - Edit Contact\n3 - Delete Contact\n4 - View Contacts\n5 - Search Address Book\n6 - Exit\n")
    
    # Keep prompting the user until a valid answer is given
    # (add counter for when user exceed 5 reask the question and give sggestions)
    # accept string inputs like add contact or edit contact
    options = [str(number) for number in range(1,7)]
    while True:
        option = input("Choose an option:  ").lstrip("0")
        if option in options:
            break

    # Prompt again depending on what the user want to do
    if option == options[0]:
        add_contact()
    
    elif option == options[1]:
        edit_contact()
    
    elif option == options[2]:
        delete_contact()
    
    elif option == options[3]:
        view_contact()
    
    elif option == options[4]:
        search_address_book()
    
    else:
        sys.exit("The program is closing. Thank you!")

    
    
def add_contact():
    # Prompt for first name, last name, address, and contact number
    print("\nFill up the details for the new contact")
    
    first_name = get_name("first_name")
    last_name = get_name("last_name")
    # address = get_address()

    print(first_name, last_name)
    print("successfully got the name")
    # main_menu()






        
    

            
def edit_contact():
    pass

def delete_contact():
    pass

def view_contact():
    pass

def search_address_book():
    pass










if __name__ == "__main__":
	main_menu()