"""
Description: Password Generator GUI
Author: Azime Ulker    
Date Created: 2024-01-18
"""

import random
from guizero import App, Text, TextBox, PushButton, info, Picture


def do_generating():
    ''' do_generating class represents generated passwords. '''

    # List to store generated passwords
    passwords = ["Your passwords:"]

    # Characters to be usedin generating passwords
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.,-'
    
    # Number of passwords to generate, extracted from the input TextBox
    number = int(number_of_password.value)

    # Length of each pasword, extracted from the input TextBox
    length = int(password_length.value)

    # Loop to generate the specified number of passwords
    for p in range(number):
        password = ''
        
        # Loop to generate each password with the specified length
        for c in range(length):
            password += random.choice(chars)

        # Append the generated password to the list
        passwords.append(str(password))  

    # Combine the passwords into a string with newline characters
    string = "\n\n".join(passwords)  

    # Display the generated passwords in an information dialog
    info("Passwords", string)

# Create the main application window
app = App(title="Password Generator", width=400, height=500, layout="auto")

# Widgets for the user interface
Welcome_message = Text(app, text='\nWelcome to password generator', size=20, font="Times New Roman", color="brown")
number_asking = Text(app, text="\nHow many passwords?")
number_of_password = TextBox(app, width=30)
length_asking = Text(app, text="\n\nHow many character of each password?")
password_length = TextBox(app, width=30)
get_button = PushButton(app, command=do_generating, text="Get Password", align="bottom")
get_button.bg = "lightpink"
my_gif = Picture(app, image="C:\Dev\ADEV-3005\IoT\gif.gif")

# Display the application window
app.display()
