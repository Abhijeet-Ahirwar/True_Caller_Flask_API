import sqlite3

conn = sqlite3.connect('detail.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE INFORMATIONS
         (NAME TEXT NOT NULL,
         Phone_NUmber INTEGER PRIMARY KEY NOT NULL,
         Email text UNIQUE,
         Spam numeric NOT NULL);''')

conn.execute('''CREATE TABLE SPAM
         (NAME TEXT,
         Phone_NUmber INTEGER PRIMARY KEY NOT NULL);''')
print("Table created successfully")

conn.close()
