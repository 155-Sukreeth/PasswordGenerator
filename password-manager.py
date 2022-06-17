from tkinter import *
from tkinter import messagebox
import pass_gen
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    brand_new_pass = pass_gen.new_pass()
    pass_input.insert(END, brand_new_pass)
    pyperclip.copy(brand_new_pass)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search_pass():
    web_found = web_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='error', message='There are no saved passwords')
    else:
        if web_found in data:
            user_found = data[web_found]['email']
            pass_found = data[web_found]['pass']
            messagebox.showinfo(title=web_found, message=f'Email: {user_found}\nPassword: {pass_found}')
            pyperclip.copy(pass_found)
        else:
            messagebox.showerror(title='error', message='There are no saved passwords for the given website')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    website = web_input.get()
    user = user_input.get()
    password = pass_input.get()
    new_dict = {
        website: {
            'email': user,
            'pass': password
        }
    }
    if len(website) < 1 or len(user) < 1 or len(password) < 1:
        messagebox.showerror(title='Empty fields found!!!', message='fields cannot be empty')
        return
    if messagebox.askokcancel(title=website, message=f'Re-Check details:\nEmail: {user}\nPassword: {password}'):
        try:
            with open(file='data.json', mode='r') as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file='data.json', mode='w') as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            # update old data with new data
            data.update(new_dict)
            with open(file='data.json', mode='w') as data_file:
                # write this updated data to our json file
                json.dump(data, data_file, indent=4)

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
web_input = Entry(width=32)
web_input.grid(column=1, row=1)

user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)
user_input = Entry(width=52)
user_input.insert(index=0, string='sukreeth2001@gmail.com')
user_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_input = Entry(width=32)
pass_input.grid(column=1, row=3)

# buttons
gen_button = Button(text='Generate Password', command=gen_pass)
gen_button.grid(column=2, row=3)

add_button = Button(text='ADD Password', width=45, command=write_pass)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=15, command=search_pass)
search_button.grid(column=2, row=1)

window.mainloop()
