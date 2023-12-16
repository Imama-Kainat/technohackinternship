from tkinter import *
import string
import random
import pyperclip


def generator():
    # Define character sets
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.delete(0, END)  # delete the previous written password
        # Generate password using only small alphabets
        passwordField.insert(0, ''.join(random.sample(small_alphabets, password_length)))

    if choice.get() == 2:
        passwordField.delete(0, END)
        # Generate password using small and capital alphabets
        passwordField.insert(0, ''.join(random.sample(small_alphabets + capital_alphabets, password_length)))

    if choice.get() == 3:
        passwordField.delete(0, END)
        # Generate password using all character sets
        passwordField.insert(0, ''.join(random.sample(all_characters, password_length)))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()  # Create a Tkinter window
root.title('🔐 Password Generator')
root.geometry('400x300')
root.config(bg='#2c3e50')  # Set background color to a vibrant blue

choice = IntVar()  # Variable to store the choice of password strength
Font = ('Helvetica', 13, 'bold')  # Change the font to Helvetica

# Label for the password generator title
passwordLabel = Label(root, text='🔐 Password Generator', font=('Helvetica', 20, 'bold'), bg='#3498db', fg='white')
passwordLabel.grid(pady=10)

# Radio buttons for choosing password strength
weakRadioButton = Radiobutton(root, text='Weak 🌱', value=1, variable=choice, font=Font)
weakRadioButton.grid(pady=5)

mediumRadioButton = Radiobutton(root, text='Medium 🌳', value=2, variable=choice, font=Font)
mediumRadioButton.grid(pady=5)

strongRadioButton = Radiobutton(root, text='Strong 💪', value=3, variable=choice, font=Font)
strongRadioButton.grid(pady=5)

# Label for selecting password length
lengthLabel = Label(root, text='Password Length 📏', font=Font, bg='#3498db', fg='white')
lengthLabel.grid(pady=5)

# Spinbox for choosing password length
length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

# Button to generate password
generateButton = Button(root, text='Generate 🔄', font=Font, command=generator)
generateButton.grid(pady=5)

# Entry field to display generated password
passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

# Button to copy generated password to clipboard
copyButton = Button(root, text='Copy 📋', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()  # Run the Tkinter event loop
