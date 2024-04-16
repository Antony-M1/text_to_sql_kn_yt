import sqlite3


## connect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor is responsible to insert, create, delete, read records from the db
cursor = connection.cursor()

## Create the table
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(150), CLASS VARCHAR(150), SECTION VARCHAR(150), MARKS INT);
"""

# Execute the SQL query
cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')


## Display all the records
print("The inserted recored are")

data = cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(data)


## Close the connection

connection.commit()
connection.close()