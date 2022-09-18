from tkinter import *
from tkinter import messagebox   # we import it seperately bcoz ?* imports classes and this is not a class
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():

    password_list = []
    for char in range(randint(8, 10)):
      password_list.append(choice(letters))

    for char in range(randint(2, 4)):
      password_list += choice(symbols)

    for char in range(randint(2, 4)):
     password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    input_password.insert(0, password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    name_website = input_website.get()
    name_email = input_email.get()
    name_password = input_password.get()

    with open('password.txt', 'w') as data:
        if len(name_website) == 0 or len(name_email) <= 3 or len(name_password) == 0:
            option = messagebox.showinfo(title="Uhh-ohh", message="Oops missed a field")
        else:
            option = messagebox.askokcancel(title="Confirm",
                                            message=f"Website: {name_website}\nEmail: {name_email}\nPassword: {name_password}\nSave?")
            if option:
                data.write(f"{name_website} || {name_email} || {name_password}\n")
                option = messagebox.showinfo(title="Success", message="Successfully Saved")
                input_password.delete(0, END)
                input_website.delete(0, END)
                data.close()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.config(bg='black',padx=10, pady=10)

# -----------------------------------------------------------------------------------|
canvas = Canvas(width=50, height=50,  highlightthickness=0)
bg = PhotoImage(file='blackpro.png')
my_lable = Label(window, image = bg)
my_lable.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------------------------------------------------------------------------
#timer_img = PhotoImage(file="")
#canvas.create_image(100, 100, image=timer_img)
#canvas.grid(row=0, column=1)

website_label = Label(text="Webiste:")
website_label.config(bg="white")
website_label.grid(row=1, column=0)

input_website=Entry(width=50)
input_website.grid(row=1, column=1 ,columnspan=2)
input_website.insert(0,  "xyz.com")
input_website.focus()   # Puts cursor in textbox.


email_label= Label(text="Email/Username:")
email_label.config(bg="white")
email_label.grid(row=2, column=0)

input_email=Entry(width=50)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "yourname@gmail.com")

password_label= Label(text="Password:")
password_label.config(bg="white")
password_label.grid(row=3, column=0)

input_password=Entry(width=25)
input_password.grid(row=3, column=1)
input_password.insert(0, "")

password_button=Button(text='Generate Password',command=password_generator)
password_button.grid(row=3, column=2)

add_button=Button(text='Add', width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
