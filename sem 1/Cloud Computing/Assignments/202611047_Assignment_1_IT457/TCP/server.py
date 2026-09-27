import socket
# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost (127.0.0.1) and port 8080
server.bind(("127.0.0.1", 8080))

# Listen for incoming connections
server.listen(1)
print("TCP Server started...")
print("Waiting for client...")
# Accept an incoming connection from the client
client, address = server.accept()
print("Client connected!")

# Infinite loop to keep processing client's questions
while True:
    # Receive the question from the client (up to 1024 bytes) and decode it
    question = client.recv(1024).decode()

    # If no data is received, break the loop
    if not question:
        break

    # If client sends "exit", break the loop to close the connection
    if question == "exit":
        break

    # Default answer if the question is not found in the file
    answer = "Question not found."

    # Open the Q&A file in read mode
    file = open("qa.txt", "r")

    # Read the file line by line
    for line in file:
        # Split the line into question and answer using the '|' delimiter
        parts = line.strip().split("|", 1)

        # Ensure the line has exactly two parts (Question and Answer)
        if len(parts) == 2:
            storedQuestion = parts[0]
            storedAnswer = parts[1]

            # If the received question matches the stored question, set the answer
            if question == storedQuestion:
                answer = storedAnswer
                break # Stop searching once the match is found

    # Close the file after reading
    file.close()
    print("Question:", question)
    print("Answer:", answer)

    # Encode and send the answer back to the client
    client.send(answer.encode())

# Close the client connection and server socket
client.close()
server.close()