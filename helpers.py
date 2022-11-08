from string import digits, punctuation

def get_first_name():
    first_name = input("First name:  ")

    # Ensure first name has no numbers or any special characters
    for character in first_name:
        if character in digits or character in punctuation:
            print("\nName cannot have a number or special characters. Try Again.")
            get_first_name()


def get_last_name():
    last_name = input("Last name:  ")

    # Ensure last name has no numbers or any special characters
    for character in last_name:
        if character in digits or character in punctuation:
            print("\nName cannot have a number or special characters. Try Again.")
            get_last_name()
