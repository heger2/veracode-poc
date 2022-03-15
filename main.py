import sys
import mysql.connector

name = sys.argv[1]

db = mysql.connector.connect(
    host="localhost",
    user="foo",
    password="bar"
)


cursor = db.cursor()
# Added to test if code analysis tools find the injections vuln
cursor.execute(f'INSERT INTO footable (name) VALUES ("{name}"")')
cursor.execute('INSERT INTO footable (name) VALUES ("' + name +'")')
db.commit()
