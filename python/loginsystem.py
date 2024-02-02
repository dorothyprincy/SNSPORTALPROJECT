from tkinter import*
import tkinter as tk
import mysql.connector 
from tkinter import  messagebox
from subprocess import call

#connect to Database MYSQL workbench

mysqldb= mysql.connector.connect(
      host="localhost",
        user="root", 
        password="Dorothy.G@1507",
          database="snsportal",
          port='3306'
    )
mycursor = mysqldb.cursor()

# def initialize_connection():
#    username=e1.get()
#    password=e2.get()
   

#    sql= 'select * from `snsportal.employeedetails`  where `username` = %s and passowrd - %s'
#    mycursor.execute(sql, [(username), (password)])
#    results = mycursor.fetchall()
#    if results:
#       messagebox.showinfo("", "Login Success")
#       root.destroy()
#       return True
   
#    else:
#       messagebox.showinfo("","Incorrect Username and Password")
#       return False


root = Tk()
root.title("SnS Portal Login")
root.geometry("300x200")
global e1
global e2

#Label1
Label(root, text="SnS Portal", font=('Times New Roman', 30, 'bold')).grid(row=0, column=3)

#Label2
e1= Label(root, text="Username")
e2= Label(root, text="Password")

e1.grid(row=1, column=2)
e2.grid(row=2, column=2)

#Entry
e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e2.config(show="*")
#button
Button(root, text="Submit", command="initialize_connection", height=3, width=10).place(x=100, y=100)


def initialize_connection():
   username=e1.get()
   password=e2.get()
   print(username,password)

   sql= 'select * from `snsportal.employeedetails`  where `username` = %s and passowrd - %s'
   mycursor.execute(sql, [(username), (password)])
   results = mycursor.fetchall()
   if results:
      messagebox.showinfo("", "Login Success")
      root.destroy()
      return True
   
   else:
      messagebox.showinfo("","Incorrect Username and Password")
      return False


# #connect to Database MYSQL workbench
# def initialize_connection():
#    mysqldb= mysql.connector.connect(
#       host="127.0.0.1",
#         user="root", 
#         password="Dorothy.G@1507",
#           database="snsportal"
#     )
#    mycursor = mysqldb.cursor()
#    username=e1.get()
#    password=e2.get()
#    mysqldb.commint()

#    sql= "select * from snsportal.employeedetails  where username = %s and passowrd - %s"
#    mycursor.execute(sql, [(username), (password)])
#    results = mycursor.fetchall()
#    if results:
#       messagebox.showinfo("", "Login Success")
#       root.destroy()
#       return True
   
#    else:
#       messagebox.showinfo("","Incorrect Username and Password")
#       return False
#    conn.commit()
   

# #define the  Button
# def login(cursor, data):
#    cursor.execute (f"SELECT * from snsportal.employeedetails where username ='{data["username"]}'")
#    cursor.execute (f"SELECT * from snsportal.employeedetails where password ='{data["password"]}'")
#    print(cursor.fetchall())

# def submit(self):
#    data ={}
#    data["username"] = e1.get()
#    data["password"] = e2.get()
#    login(data)


root.mainloop()