from tkinter import *
from tkinter import messagebox
import pass_gen
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    brand_new_pass = pass_gen.new_pass()
    pass_input.insert(END, brand_new_pass)
    pyperclip.copy(brand_new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    website = web_input.get()
    user = user_input.get()
    password = pass_input.get()
    if len(website) < 1 or len(user) < 1 or len(password) < 1:
        messagebox.showerror(title='Empty fields found!!!', message='fields cannot be empty')
        return
    if messagebox.askokcancel(title=website, message=f'Re-Check details:\nEmail: {user}\nPassword: {password}'):
        with open(file='passwords.txt', mode='a') as passwords:
            passwords.write(website + ' | ' + user + ' | ' + password + '\n')
            # both the start index and end index are inclusive
            web_input.delete(0, 'end')
            # user_input.delete()
            pass_input.delete(0, 'end')
            messagebox.showinfo(title='Success', message='Password added!!')
            pyperclip.copy(password)
    else:
        web_input.delete(0, 'end')
        # user_input.delete()
        pass_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

# Logo
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(column=1, row=0)

# input
web_label = Label(text="Website")
web_label.grid(column=0, row=1)
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=2)

user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)
user_input = Entry(width=50)
user_input.insert(index=0, string='mydefaultaccount@gmail.com')
user_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_input = Entry(width=32)
pass_input.grid(column=1, row=3)

# buttons
gen_button = Button(text='Generate Password', command=gen_pass)
gen_button.grid(column=2, row=3)

add_button = Button(text='ADD Password', width=43, command=write_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
