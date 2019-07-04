import sqlite3
from flask import Flask, g, render_template, config, request
import os

app = Flask(__name__)

@app.route('/register',methods = ['POST', 'GET'])
def register():
	if request.method == 'GET':
		return render_template('forms/index.html')
	elif request.method == 'POST':
		try:
			name = request.form['name']
			phone = request.form['num']
			email = request.form['email']
			spam = 0
			with sqlite3.connect("detail.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO INFORMATIONS (NAME,Phone_NUmber,Email,Spam) VALUES (?,?,?,?)",(name,phone,email,spam) )
				con.commit()
				msg="ADDED SUCCESSFULLY"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("forms/result.html",msg = msg)
			con.close()

@app.route('/global',methods = ['POST', 'GET'])
def hello_world():
	if request.method == 'GET':
		conn = sqlite3.connect('detail.db')
		cursor = conn.execute('SELECT NAME ,Phone_NUmber,Email,Spam from INFORMATIONS;')
		authors = [dict(Name=row[0],Phone_NUmber=row[1],Email=row[2],Spam_Status=row[3]) for row in cursor.fetchall()]
		return str(authors)

@app.route('/spamlist',methods = ['POST', 'GET'])
def spamlist():
	if request.method == 'GET':
		conn = sqlite3.connect('detail.db')
		cursor = conn.execute('SELECT NAME ,Phone_NUmber from SPAM;')
		info = [dict(Name=row[0],Phone_NUmber=row[1]) for row in cursor.fetchall()]
		return str(info)

@app.route('/search',methods = ['POST', 'GET'])
def search():
	if request.method == 'GET':
		return render_template('forms/search.html')
	elif request.method == 'POST':
		name = request.form['name']
		phone = request.form['num']
		conn = sqlite3.connect('detail.db')
		if phone != "":
			cursor = conn.execute("SELECT NAME,Phone_NUmber,Email,Spam from INFORMATIONS where Phone_NUmber = (?);",(phone,))
			authors = [dict(Name=row[0],Phone_NUmber=row[1],Email=row[2],Spam_Status=row[3]) for row in cursor.fetchall()]
			if authors is not None:
				return str(authors)
			else:
				cursor = conn.execute("SELECT NAME,Phone_NUmber from SPAM where Phone_NUmber = (?);",(phone,))
				authors = [dict(Name=row[0],Phone_NUmber=row[1]) for row in cursor.fetchall()]
				if authors is not None:
					return str(authors)
				else:
					return "NOT FOUND"
		else:
			cursor = conn.execute("SELECT NAME,Phone_NUmber,Email,Spam from INFORMATIONS where NAME = (?);",(name,))
			authors = [dict(Name=row[0],Phone_NUmber=row[1],Email=row[2],Spam_Status=row[3]) for row in cursor.fetchall()]
			if authors is not None:
				return str(authors)
	conn.close()

@app.route('/spam',methods = ['POST', 'GET'])
def spam():
	if request.method == 'GET':
		return render_template('forms/spam.html')
	elif request.method == 'POST':
		try:
			name = request.form['name']
			phone = request.form['num']
			with sqlite3.connect("detail.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO SPAM (NAME,Phone_NUmber) VALUES (?,?);",(name,phone))
				cursor = con.execute("SELECT NAME ,Phone_NUmber,Email,Spam from INFORMATIONS;")
				authors = [dict(Name=row[0],Phone_NUmber=row[1],Email=row[2],Spam_Status=row[3]) for row in cursor.fetchall()]
				temp=[]
				for a in range(0,len(authors)):
					temp.append(authors[a]['Phone_NUmber'])
				if phone in temp:
					con.execute("UPDATE INFORMATIONS SET Spam=? WHERE Phone_NUmber=?;",(1,phone))
				msg="ADDED SUCCESSFULLY"
				con.commit()
		except:
			con.rollback()
			msg = "ERROR IN INSERT OPERATION"
		finally:
			return render_template("forms/result.html",msg = msg)
			con.close()



if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT',2010))
    app.run(host=host, port=port)
