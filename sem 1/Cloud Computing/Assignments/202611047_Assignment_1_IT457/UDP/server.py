import socket
import zlib
# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to localhost (127.0.0.1) and port 8081
server.bind(("127.0.0.1", 8081))

print("UDP Server started...")
print("Waiting for packets...")

# Infinite loop to keep receiving packets
while True:
    # Receive data and client address (buffer size 1024)
    packet, address = server.recvfrom(1024)
    packet = packet.decode()
    
    # Split the received packet into message and checksum
    parts = packet.split("|")
    
    if len(parts) == 2:
        message = parts[0]
        received_checksum = int(parts[1])
        
        # Calculate the 32-bit checksum (CRC32) of the received message
        calculated_checksum = zlib.crc32(message.encode())
        
        # Check for errors by comparing received checksum with calculated checksum
        if received_checksum == calculated_checksum:
            print(f"\n[SUCCESS] Valid message from {address}: {message}")
            # Send success response to client
            server.sendto(b"Packet accepted: No errors found.", address)
        else:
            print(f"\n[ERROR] Corrupted packet received from {address}!")
            # Send error response to client
            server.sendto(b"Error: Packet corrupted during transmission!", address)
