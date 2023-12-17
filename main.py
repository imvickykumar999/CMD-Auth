
import requests
import sqlite3 as sql

def crud_table():
	con = sql.connect('db_web.db')
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS users")

	sql3 ='''
CREATE TABLE "users" (
"UID"	    INTEGER PRIMARY KEY AUTOINCREMENT,
"UNAME"	    TEXT,
"NAME"	    TEXT,
"FILE"	    TEXT,
"CONTACT"	TEXT
)'''

	cur.execute(sql3)
	con.commit()
	con.close()


def auth_table():
	con = sql.connect('db_sample.db')
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS users")

	sql3 ='''
CREATE TABLE "users" (
"UID"   INTEGER PRIMARY KEY AUTOINCREMENT,
"UNAME" varchar(50) NOT NULL,
"EMAIL" varchar(50) NOT NULL,
"UPASS" varchar(50) NOT NULL
)'''

	cur.execute(sql3)
	con.commit()
	con.close()
      

def get_req():
    # http://127.0.0.1:5000/delete_user/1
    link = input('\nEnter link : ')

    req = requests.get(link)
    print(req.text)



def post_req():
    # http://127.0.0.1:5000/edit_user/1
    link = input('\nEnter link : ')

    payload = {
        "uname": '2000', 
        "contact": "America", 
        "name": "1 Dollar"
    }

    header = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    } 

    response_decoded = requests.post(link, data=payload, headers=header)
    print(response_decoded.text)


# get_req()
# post_req()
