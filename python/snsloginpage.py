from tkinter import*
import tkinter as tk
from tkinter import  messagebox
import mysql.connector 


def initialize_connection():
    username=user.get()
    password=code.get()
    print(username, password)

    if (username=="") or (password==""):
      messagebox.showinfo("entry error","type Username or Password")
      messagebox.showinfo("", "Login Success")
      root.destroy()
      return True
   
    else:
        try:
            mysqldb= mysql.connector.connect(
             host="localhost",
             username="root", 
             password="Dorothy.G@1507",
             database="snsportal"
               )
            mycursor = mysqldb.cursor()
            print("connected to database")
 
        except:
            messagebox.showinfo("connection", "Database connection not stablish!!")
            return
        command="use snsportal"
        mycursor.execute(command)

        command="select * from snsportal.snsemployee where username=%s and password=%s"
        mycursor.execute(command,(username,password))
        myresult =mycursor.fetchone()
        print(myresult)

        if myresult==None:
            messagebox.showinfo("invalid", "Invalid username and password")

        else:
            messagebox.showinfo("Login", "Successfully Login!!" )
            root.destroy()
            import leavepage
        
        


background="white"
root = Tk()
root.title("SnS Portal Login")
root.geometry("300x200")
root.config(bg=background)
root.resizable(False,False)
global user
global code

Label(root, text="SnS Portal", font=('Times New Roman', 30, 'bold')).grid(row=0, column=3)

#username_enter
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')   


def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    
    if code.get()=='':
        code.insert(0,'password')           

user= Label(root, text="Username")
code= Label(root, text="Password")

user.grid(row=1, column=2)
code.grid(row=2, column=2)

user = Entry(root)
code = Entry(root)

user.grid(row=1, column=3)
code.grid(row=2, column=3)
code.config(show="*")

user.insert (0,'username')
code.insert (0,'password')

user.bind("<FocusIn>", user_enter )
user.bind("<FocusOut>", user_leave )

code.bind("<FocusIn>", password_enter )
code.bind("<FocusOut>", password_leave )

#button


loginButton=Button(root, text="Submit", height=3, width=10, command=initialize_connection)
loginButton.place(x=100, y=100)


   
root.mainloop()