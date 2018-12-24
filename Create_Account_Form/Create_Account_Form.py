def main():
    print("Please, fill in to create contact form here")
    full_name = get_full_name()
    password = get_password()    
    email = get_email()
    phone_number = get_phone_number()
    # add the first name in to the message greedy below here
    first_name = get_first_name(full_name)
    print()
    print("Hi " + first_name + ", thanks for creating an account.")             
    print("We will call you on this number to contact you: " + phone_number)


# check for function have first and last name here   
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:     # check for space between first and last name
            return name
        else:
            print("You must enter your full name.")


#  use the first name to greedy message  
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


# check the password with number, capital word, and count letters greater than 8 letters   
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password


# find @ and dot in the email to pass
def get_email():
    while True:
        email = input("Enter email address:   ").strip()
        at_index = email.find("@")
        dot_index = email.find(".", at_index)
        if at_index == -1 or dot_index == -1:
            print("Please enter a valid email address.")
        else:
            return email


# count the phone number has to be 10 number and format to (555)555-5555
def get_phone_number():
    while True:
        phone_number = input("Enter phone number:    ").strip()
        for char in " -().":        # loop each number and symbol and two line to replace it
            phone_number = phone_number.replace(char, "")
        if len(phone_number) != 10 or phone_number.isdigit() == False:   #check number = 10 and is number
            print("Please enter a 10-digit phone number.")
        else:
            # format to phone number format (555)555-5555
            phone_number = "(" + phone_number[0:3] + ")" + phone_number[3:6] + "-" + phone_number[6:]
            return phone_number

        
if __name__ == "__main__":
    main()
