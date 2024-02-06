from tkinter import*
from tkinter import  messagebox
import mysql.connector

def initialize_connection():
    username=e1.get()
    password=e2.get()
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
             user="root", 
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
            messagebox.showinfo("Login", "Successfully Login!!")

root = Tk()
root.title("SnS Portal Login")
root.geometry("300x200")

Label(root, text="SnS Portal", font=('Times New Roman', 30, 'bold')).grid(row=0, column=3)

#username_enter
def username_enter():
    e1.delete(0,'end')

def username_exit():
    name=e1.get()
    if name=='':
        e1.insert(0,'')   


def password_enter():
    e2.delete(0,'end')

def password_exit():
    
    if e2.get()=='':
        e2.insert(0,'')           

e1= Label(root, text="Username")
e2= Label(root, text="Password")

e1.grid(row=1, column=2)
e2.grid(row=2, column=2)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e2.config(show="*")

e1.insert (0,'')
e2.insert (0,'')

e1.bind("<FocusIn>", username_enter )
e1.bind("<FocusOut>", username_exit )

e2.bind("<FocusIn>", password_enter )
e2.bind("<FocusOut>", password_exit )

#button
loginButton=Button(root, text="Submit", command="initialize_connection", height=3, width=10).place(x=100, y=100)

root.mainloop()
