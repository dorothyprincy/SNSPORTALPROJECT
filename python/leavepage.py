import tkinter as tk


root = tk.Tk()
root.geometry('500x400')
root.title('SnS Portal')



def hide_indicators():
    Request_indicate.config(bg='lightgray')
    Response_indicate.config(bg='lightgray')

def indicate(lb):
    hide_indicators()
    lb.config(bg='black')
    


options_frame = tk.Frame(root, bg='lightgray')

Request= tk.Button(options_frame, text='Request',font=('bold',15),fg='black',bd=0,bg='lightgray',command=lambda:indicate(Request_indicate)) 
Request.place(x=10,y=50)  
clicked = tk.StringVar()
OptionMenu = tk.OptionMenu(root,clicked,"Leave","Permission","payroll") 
OptionMenu.pack() 
Request_indicate = tk.Label(options_frame,text='',bg='lightgray')
Request_indicate.place(x=10,y=50,width=3,height=30)



Response= tk.Button(options_frame, text='Response',font=('bold',15),fg='black',bd=0,bg='lightgray',command=lambda:indicate(Response_indicate)) 
Response.place(x=10,y=100) 
Response_indicate = tk.Label(options_frame,text='',bg='lightgray')
Response_indicate.place(x=10,y=100,width=3,height=30) 

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=150,height=400)


main_frame = tk.Frame(root,highlightbackground='black',highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)



root.mainloop()