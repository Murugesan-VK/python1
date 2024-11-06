import sqlite3

# Connect to the database (or create one if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO students (name, age) VALUES ('John Doe', 21)")

# Commit the transaction
connection.commit()

# Fetch and display data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()

