import tkinter
import Back_End_Helper
from tkinter import messagebox

loginData = {"UserID": None, "roleId": False}

def Login_Window():
    global loginData
    window = tkinter.Tk()
    window.title("Login form")
    window.geometry('285x320')
    window.configure(bg='#FFD1DC')
    window.resizable(False,False)


    def Validate_Credentials():
        global loginData
        def show_error():
            messagebox.showerror("Error", "Incorrect Username or Password. Please Try Again")
        backEndClass = Back_End_Helper.Validate_Credentials(username_entry.get(), password_entry.get())
        userData = backEndClass.Execute_Command()
        
        backEndClass = Back_End_Helper.Log_Usage_Record()
        if (userData != False):
            loginData["UserID"] = userData["UserID"]
            loginData["roleId"] = userData["Role_ID"]
            backEndClass.Create_Login_Event(userData["UserID"], username_entry.get(), userData["Role_ID"], True)
            window.destroy()
        else:
            backEndClass.Create_Login_Event(None, username_entry.get(), None, False)
            show_error()
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

        
    #Creating widgets
    login_label = tkinter.Label(window, text="Login", bg='#FFD1DC', font=('Roboto', 30))
    username_label = tkinter.Label(window, text="Username", bg='#FFD1DC', font=("Roboto", 12))
    username_entry = tkinter.Entry(window, font=("Roboto", 12),)
    password_entry = tkinter.Entry(window, show="*", font=("Roboto", 12))
    password_label = tkinter.Label(window, text="Password", bg='#FFD1DC', font=("Roboto", 12))
    login_button = tkinter.Button(window, text="Login", bg="#C11C84", command=Validate_Credentials)


    #Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky= "news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0, pady=20)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    window.mainloop()

    return loginData
