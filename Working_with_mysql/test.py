import mysql.connector as mysql

mydb = mysql.connect(
    host='localhost',
    user='root',
    passwd='Nazianzen1997',
    database='testdb'
)

mycur = mydb.cursor()



'''
# Query pointer
mycur = mydb.cursor()

# Drop table
sql = 'DROP TABLE IF EXISTS students'

mycur.execute(sql)

mydb.commit()

# Delete
sql = 'DELETE FROM students WHERE name = "Emma"'

mycur.execute(sql)

mydb.commit()

# Wildcards
sql = 'SELECT * FROM students WHERE name LIKE "%ar%"'

mycur.execute(sql)

result = mycur.fetchall()

for row in result:
    print(row)

# WHERE with placeholders
sql = 'SELECT * FROM students WHERE name = %s'

mycur.execute(sql, ('Emma',))

result = mycur.fetchall()

for row in result:
    print(row)

# Limit
sql = 'SELECT * FROM students LIMIT 3 OFFSET 1'

mycur.execute(sql)

result = mycur.fetchall()

for re in result:
    print(re)

# Update
sql = 'UPDATE students SET age = 20 WHERE name = "Emma"'

mycur.execute(sql)

mydb.commit()


# Fetchone
mycur.execute('SELECT * FROM students')

result = mycur.fetchone()

for row in result:
    print(row)

# Select
sql = 'SELECT * FROM students ORDER BY name DESC'

mycur.execute(sql)

result = mycur.fetchall()

for re in result:
    print(re)

# Insert
sql_formula = 'INSERT INTO students(name, age) VALUES(%s, %s)'
students = [('Bob', 18),
            ('Arinze', 23),
            ('Amanda', 20),
            ('Emma', 19),
            ('Richard', 21),
            ]

# mycur.execute(sql_formula, student1)

mycur.executemany(sql_formula, students)

mydb.commit()

# mycur.execute('CREATE DATABASE testdb')
# mycur.execute('SHOW DATABASES')
# mycur.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(11))')
# mycur.execute('SHOW TABLES')

# for db in mycur:
#    print(db)
'''