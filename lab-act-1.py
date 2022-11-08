"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

import cs50
import sys

def main():
    print("Main Menu\nWhat would you like  to do?")
    print("1 - Add Contact\n2 - Edit Contact\n3 - Delete Contact\n4 - View Contacts\n5 - Search Address Book\n6 - Exit\n")
    
    # Keep prompting the user until a valid answer is given
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
    pass
            
def edit_contact():
    pass

def delete_contact():
    pass

def view_contact():
    pass

def search_address_book():
    pass










if __name__ == "__main__":
	main()