import tkinter
window = tkinter.Tk()
window.title("Login form")
window.geometry('285x320')
window.configure(bg='#FFD1DC')
window.resizable(False,False)

#Creating widgets
login_label = tkinter.Label(window, text="Login", bg='#FFD1DC', font=('Roboto', 30))
username_label = tkinter.Label(window, text="Username", bg='#FFD1DC', font=("Roboto", 12))
username_entry = tkinter.Entry(window, font=("Roboto", 12),)
password_entry = tkinter.Entry(window, show="*", font=("Roboto", 12))
password_label = tkinter.Label(window, text="Password", bg='#FFD1DC', font=("Roboto", 12))
login_button = tkinter.Button(window, text="Login", bg="#C11C84")


#placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky= "news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0, pady=20)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()
