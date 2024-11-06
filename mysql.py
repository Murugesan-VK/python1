import mysql.connector

# Replace with your actual MySQL credentials
connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Test if connection was successful
if connection.is_connected():
    print("Connection successful!")

# Close the connection
connection.close()
