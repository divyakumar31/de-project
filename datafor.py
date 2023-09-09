import sqlite3
con = sqlite3.connect('passdetails.sql')
mycursor = con.cursor()
# mycursor.execute('CREATE TABLE userlogindetails (username varchar(20) NOT NULL PRIMARY KEY,password text NOT NULL, useremail varchar(100))')

# Schema Of usersdetails(for applypass) table: 
# mycursor.execute('CREATE TABLE userdetails ( name text not null, contactno number(12) not null, email varchar2(100) not null, college text not null, userimage text not null, username varchar(20))')

# mycursor.execute("ALTER TABLE userdetails ADD username varchar(20)")

# mycursor.execute("ALTER TABLE userdetails ADD PRIMARYKEY username")
# Schema Of users table: 
# con.execute('''CREATE TABLE users
#             (name text not null,
#             passtype text not null,
#             phonenumber number(10) not null,
#             cardnumber number(12) primary key not null,
#             passlastdate date,
#             cvvnumber int not null)''')
# mycursor.execute(''' DELETE FROM users WHERE cvvnumber = 123 ''')


# Schema of registeruser table:
# mycursor.execute('''CREATE TABLE registeruser
#                  (username text primary key not null,
#                   password text not null)''')
# print("Table created")
# mycursor.execute(''' INSERT INTO registeruser (username, password) VALUES ("divyakumar31", "divyakumar123") ''')
# mycursor.execute(''' INSERT INTO registeruser (username, password) VALUES ("devapatel5634", "devapatel56") ''')

# mycursor.execute(''' SELECT * FROM userlogindetails ''')

# mycursor.execute("DROP TABLE userdetails")
mycursor.execute(''' SELECT * FROM userdetails ''')
# mycursor.execute("DELETE FROM userdetails WHERE username='dp123'")
# mycursor.execute(''' SELECT * FROM userlogindetails WHERE username="dp123"''')

conresult = mycursor.fetchall()
# conresult = mycursor.fetchone()

for i in range(conresult.__len__()):
    print(conresult[i])

# print(conresult)

# print(conresult[1])
# print(conresult[1])
con.commit()
con.close()
print("Done")