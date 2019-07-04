#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('detail.db')
print("Opened database successfully")
name="Paul"

cursor = conn.execute("SELECT NAME,Phone_NUmber,Email from INFORMATION where NAME = (?);",(name,))
for row in cursor:
   print("NAME = ", row[0])
   print("Phone_NUmber = ", row[1])
   print("Email = ", row[2], "\n")

print("Operation done successfully")
conn.close()