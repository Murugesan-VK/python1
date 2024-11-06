import socket

# Set up server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Bind to local host and port 12345
server_socket.listen(1)  # Allow 1 connection at a time

print("Server is listening for connections...")

# Accept connection from client
connection, address = server_socket.accept()
print(f"Connected by {address}")

# Receive and print the message from the client
message = connection.recv(1024).decode()
print(f"Message from client: {message}")

# Send a response to the client
connection.send("Hello from the server!".encode())

# Close the connection
connection.close()
server_socket.close()

#client
import socket

# Set up client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to the server

# Send a message to the server
client_socket.send("Hello, server!".encode())

# Receive and print the response from the server
response = client_socket.recv(1024).decode()
print(f"Response from server: {response}")

# Close the connection
client_socket.close()
