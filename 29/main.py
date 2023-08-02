from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    #Password Generator Project
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_pass = [choice(letters) for _ in range(randint(8,10))]
    symbols_pass = [choice(symbols) for _ in range(randint(2,4))]
    numbers_pass = [choice(numbers) for _ in range(randint(2,4))]

    password_list = letters_pass + symbols_pass + numbers_pass
    shuffle(password_list)
    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwod():
    data_web = str(input_web.get())
    data_email = str(input_email.get())
    data_password = str(input_password.get())
    data = {
        data_web:{
            "email":data_email,
            "password":data_password
        }
    }
    
    check_data = len(data_email) == 0 or len(data_password) == 0 or len(data_web) == 0
    
    if check_data:
        messagebox.showwarning(title='Warning!!', message="Uncompleted info")
    else:
        is_ok = messagebox.askokcancel(title=data_web, message=f"There are the details entered:\n Email: {data_email}\n Password: {data_password}\n It's ok to save?")
        if is_ok:
            try:
                with open('29/data.json', mode='r') as file:
                    dat = json.load(file)
            except FileNotFoundError:
                with open('29/data.json', mode="w") as file:
                    json.dump(data, file, indent=4)
            else:
                dat.update(data)
                with open('29/data.json', mode="w") as file:
                    json.dump(dat, file, indent=4)
            finally:
                    input_email.delete(0, END)
                    input_password.delete(0, END)
                    input_web.delete(0, END)

#search functionality

def find_password():
    data_web = str(input_web.get())
    try:
        with open('29/data.json', mode='r') as file:
            dat = json.load(file)
            web = dat[data_web]
            email = web['email']
            passwors = web['password']
    except FileNotFoundError:
        messagebox.showwarning(title='Warning!!', message="No data file found")
    else:
        if data_web in dat:
            messagebox.showinfo(title=f"{data_web}", message=f"email: {email} \npassword: {passwors}")
        else:
            messagebox.showwarning(title='Warning!!', message=f"No details for {data_web}")
# ---------------------------- UI SETUP ------------------------------- #

WIDHT = 40

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=40,bg="white")
canvas = Canvas(width=155, height=220, highlightthickness=0, bg="white")
lock_img = PhotoImage(file="29/logo.png")
canvas.create_image(100,112,image= lock_img)
canvas.grid(row=1,column=2)
#labels
web = Label(text="Website",bg="white",pady=5)
web.grid(row=2,column=1)
email = Label(text="EMAIL/Username",bg="white",pady=5)
email.grid(row=3,column=1)
password = Label(text="Password",bg="white",pady=5)
password.grid(row=4,column=1)
#buttons 
btn_generate_pass = Button(text="Generate password", highlightthickness=0, bg="white",command=gen_password,width=16)
btn_generate_pass.grid(row=4,column=3)
btn_add =Button(text="Add", highlightthickness=0, bg="white",pady=5, command=save_passwod, width=WIDHT)
btn_add.grid(row=5,column=2,columnspan=2)
btn_search =Button(text="search", highlightthickness=0, bg="white", width=16, command=find_password)
btn_search.grid(row=2,column=3)
#inputs
input_web = Entry(width=20)
input_web.grid(row=2,column=2)
input_email = Entry(width=WIDHT)
input_email.grid(row=3,column=2,columnspan=2)
input_password = Entry(width=20)
input_password.grid(row=4,column=2)


window.mainloop()