# Flask_Api_Like_TrueCaller
User can Register,search and Block a existing or non existing user based on name or phone number.
Open command prompt or linux shell
then,
install python packages 
1.flask,
2.request,
3.config
using command <pip install package_name>


now, change the directory to library

IN LIBRARY FOLDER run file named main.py

1. localhost:2010/register
	is used to add a new user
	fill the form and press enter.


**AT ANY POINT IF YOU WANT TO CHECK THE GLOBAL DATABASE open link localhost:2010/global
  using the command <python test_global_database.py>
  this will the show the database information



2. localhost:2010/spam
	is used to spam someone 
	fill the form and press enter.

**AT ANY POINT IF YOU WANT TO CHECK THE SPAM DATABASE open link localhost:2010/spamlist
  using the command <python test_spam_database.py>
  this will the show the spam user information



3.localhost:2010/search
	is used to search the user
	fill the form and press enter.
	information will be shown.


**Sqlite3 database is used.
