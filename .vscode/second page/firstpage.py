import getpass

users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
}

username = input("Enter your username: ")

if username in users:
    password = getpass.getpass("Enter your password: ")
    
    if password == users[username]:
        print("Access granted.")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # from tkinter import *
# from tkinter import messagebox
 
# def login():
#     username= Entry.get()
#     password= Entry.get()
    
#     if(username==" and password="):
#         messagebox.showinfo("","blank not allowed")
#     elif(username=="hemapriya"and password="@hema1019"):
#         messagebox.showinfo("","login sucess")   
#     else:
#         messagebox.showinfo("","incorrect username and password")    
# root=Tk()
# root.title("login")
# root.geometry("300*200")

# global Entry1
# global Entry2  

# Label(root,text="username").place(x=20,y=20)
# Label(root,text="password").place(x=20,y=70)      
         
# Entry1=Entry(root,bd=5)
# Entry1.place(x=140,y=20)   

# Entry2=Entry(root,bd=5)
# Entry2.place(x=140,y=70)

# Button(root,text="login",command=login,height=3,width=13,bd=6).place(x=100,y=120)   
# root.mainloop

