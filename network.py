import socket
import threading

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the host and port
    host = '127.0.0.1'  # Localhost
    port = 65432        # Arbitrary non-privileged port
    
    # Bind the socket to the address
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port", port)
    
    # Accept a connection
    conn, addr = server_socket.accept()
    print("Connection from", addr)
    
    # Receive the message
    message = conn.recv(1024).decode()
    print("Message received from client:", message)
    
    # Send a response back to the client
    response = "Message received!"
    conn.send(response.encode())
    
    # Close the connection
    conn.close()
    server_socket.close()

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the host and port
    host = '127.0.0.1'  # Server's IP address
    port = 65432        # The same port as the server
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print("Response from server:", response)
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    # Start the server in a new thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    # Give the server a moment to start
    import time
    time.sleep(1)
    
    # Start the client
    start_client()
