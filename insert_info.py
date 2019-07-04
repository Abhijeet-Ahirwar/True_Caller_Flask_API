#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('detail.db')
print("Opened database successfully")

conn.execute("INSERT INTO INFORMATION (NAME,Phone_NUmber,Email) \
      VALUES ('Paul', 9874563210, 'paul@hotmail.com')");

conn.execute("INSERT INTO INFORMATION (NAME,Phone_NUmber,Email) \
      VALUES ('Allen', 9630852741, 'allen@hotmail.com')");

conn.execute("INSERT INTO INFORMATION (NAME,Phone_NUmber,Email) \
      VALUES ('Mark', 9517846320, 'mark@hotmail.com')");

conn.commit()
print("Records created successfully")
conn.close()