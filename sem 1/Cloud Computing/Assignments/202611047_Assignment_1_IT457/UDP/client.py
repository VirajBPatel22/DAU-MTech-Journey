import socket
import zlib

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 8081)

print("UDP Client started!")

# Infinite loop to send messages to the server
while True:
    # Take message input from the user
    message = input("\nEnter message to send (or 'exit' to quit): ")
    if message == "exit":
        break
    # Calculate the 32-bit checksum of the message
    checksum = zlib.crc32(message.encode())
    
    # Artificially introduce error for testing purposes
    corrupt = input("Do you want to send a corrupted packet to test error handling? (y/n): ")
    
    if corrupt.lower() == 'y':
        # Modify the checksum to create an artificial error
        checksum = checksum + 1
        print("Artificial error introduced!")
        
    # Format the packet as "message|checksum"
    packet = f"{message}|{checksum}"
    
    # Send the packet to the server
    client.sendto(packet.encode(), server_address)
    
    # Receive the response from the server
    response, _ = client.recvfrom(1024)
    print("Server Response:", response.decode())

# Close the socket connection
client.close()