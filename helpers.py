from string import digits, punctuation

def get_name(name):
    if name == "first_name":
        input_name = input("First name:  ")
    else:
        input_name = input("Last name:  ")

    # Ensure first name has no numbers or any special characters
    for character in input_name:
        if character in digits or character in punctuation:
            print("\nName cannot have a number or special characters. Try Again.")
            return get_name(name)
    else:
        # Remove starting, ending, and trailing whitespace


        return input_name
