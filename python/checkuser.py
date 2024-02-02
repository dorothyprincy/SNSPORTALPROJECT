db={"hema":"1907","doro":"1507"}
username=input("Enter username:")
password=input("Enter password:")

for i in db.key():
    if username == i:
        
        while password != db.get(i):
            password =input\
            ("Enter your password again:")
            break
        print("Login successfully")