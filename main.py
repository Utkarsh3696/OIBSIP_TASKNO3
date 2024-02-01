
import random
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

m = Tk()
m.title("Random Password Generator")
l = Label(m, text="Random Password Generator", bg="black",
          fg="red", font=("console", 18, "bold")).place(x=40, y=10)

m.geometry("420x530")
m.configure(bg="black")

l1 = Label(m, text="Choose the Length of Password", bg="black",
           fg="blue", font=("console", 10)).place(x=120, y=60)
m.resizable(0, 0)

w = Scale(m, from_=8, to=108, orient=HORIZONTAL, tickinterval=20,
          length=300, bg="black", fg="white", font=("console", 10))
w.place(x=60, y=100)
w.set(8)


def show_values():
    print(w.get())
    Password = ''
    length = w.get()
    for i in range(w.get()):

        symbols = ['@', '#', '$', '%', '^', '&', '*', '!']
        radint = random.randint(0, 9)
        lcl = random.randint(97, 122)
        ucl = random.randint(65, 90)

        if (len(Password) == length):
            break
        Password += random.choice(symbols)
        if (len(Password) == length):
            break
        Password += chr(lcl)
        if (len(Password) == length):
            break
        Password += chr(ucl)
        if (len(Password) == length):
            break
        Password += str(radint)
        if (len(Password) == length):
            break

    variable_value.set(Password)

    # Update the Entry widget with the new variable value
    text_variable.delete(1.0, END)
    text_variable.insert(END, Password)

    print(Password)


variable_value = StringVar()

Button(m, text='Generate', command=show_values, bg="black", fg="blue",
       font=("console", 13, "bold"), width=20).place(x=100, y=190)

text_variable = Text(m, width=30, height=3, bg="gray", fg="white", font=(
    "console", 15), wrap=WORD, padx=10, pady=10)
text_variable.place(x=40, y=250)


def copy():
    value_to_copy = text_variable.get("1.0", END)
    if len(value_to_copy) >= 8:

        m.clipboard_clear()  # Clear the clipboard
        m.clipboard_append(value_to_copy)  # Append the value to the clipboard
        m.update()  # Update the clipboard

        # Show a message box to inform the user
        messagebox.showinfo(
            "Copied", f"Value '{value_to_copy}' copied to clipboard!")
    else:
        messagebox.showerror(
            "not copied", " err(1) - Empty textboard or Password is not valid so please try again...!")


def clear():
    text_variable.delete("1.0", END)


Button(m, text='Copy', command=copy, bg="black", fg="blue",
       font=("console", 12, "bold"), width=10).place(x=80, y=360)
Button(m, text='Clear', command=clear, bg="black", fg="red",
       font=("console", 12, "bold"), width=10).place(x=210, y=360)

l2 = Label(m, text="Genrated Password Contains Atleast:  ",
           bg="black", fg="red", font=("console", 8)).place(x=20, y=400)
l3 = Label(m, text="> 1 Uppercase, 1 Lowercase, 1 Number and 1 Symbol  ",
           bg="black", fg="white", font=("console", 8)).place(x=30, y=420)
l4 = Label(m, text="> Provides length of Password between 8 to 180 ",
           bg="black", fg="white", font=("console", 8)).place(x=30, y=440)
l7 = Label(m, text="----------------------------------------------------------------------------------------------------------------------",
           bg="black", fg="white", font=("console", 8)).place(x=0, y=470)


l5 = Label(m, text="PROJECT 3 @Oasis_Infobyte #Python_Programming",
           bg="black", fg="red", font=("console", 8)).place(x=70, y=490)
l6 = Label(m, text="@Utkarsh Karale", bg="black", fg="blue",
           font=("console", 8)).place(x=140, y=510)

m.mainloop()
