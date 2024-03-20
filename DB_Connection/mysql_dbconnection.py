import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pasword@01",
    database="javatechnologiesframeworks"
)

mycursor=conn.cursor()
# mycursor.execute("show databases")
# # to see all
# for i in mycursor:
#     print(i)
mycursor.execute("select * from registration.budget_details")
result =mycursor.fetchall()
my_list = list(result)
for i in my_list:
    print(i)

print("Test connection")
