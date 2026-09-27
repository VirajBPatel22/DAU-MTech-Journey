import socket

# Create a TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server running on localhost (127.0.0.1) at port 8080
client.connect(("127.0.0.1", 8080))

print("Connected to server!")

# Infinite loop to keep asking questions to the server
while True:
    
    # Take question input from the user via terminal
    question = input("\nEnter question: ")

    # Encode and send the question to the server
    client.send(question.encode())

    # If the user types "exit", break the loop to close the client
    if question == "exit":
        break

    # Receive the answer from the server (up to 1024 bytes) and decode it
    answer = client.recv(1024).decode()

    # Print the received answer from the server
    print("Server:", answer)

# Close the client socket connection
client.close()
