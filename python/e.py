import mysql.connector
conn =mysql.connector.connect(user='root', password='Dorothy.G@1507', host='localhost')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print(" Connection Successfully")
print("hi my name is dorothy")