from tkinter import * 


window = Tk()
window.title('Miles to Km')
window.minsize(width=500, height=300)

""" #label
my_label= Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
#Entry

input = Entry(width=10)
input.grid(row=3, column=4)

#button
def button_clicked():
    txt = input.get()
    my_label.config(text=f"{txt}")

button = Button(text="Click me", command=button_clicked)
button.grid(row=2, column=2)


new_button = Button(text="New Button")
new_button.grid(row=1,column=3) """
def convert():
    user_miles = int(input.get())
    result = user_miles * 1.60934
    res_km.config(text=str(round(result,2)))
input = Entry(width=15)
input.grid(row=1, column=2)
miles = Label(text="Miles")
miles.grid(row=1, column=3)
equal_to = Label(text="is equal to")
equal_to.grid(row=2,column=1)
res_km = Label(text=0)
res_km.grid(row=2,column=2)
km = Label(text="Km")
km.grid(row=2,column=3)
button = Button(text="Calculate",command=convert)
button.grid(row=3,column=2)
window.mainloop()