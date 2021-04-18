# UDPPingerClient.py
import time
from socket import *

# Setting up localhost server
IPAddress = 'localhost'
# UDP port number
portNumber = 12000

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set timeout of one second for response from server
clientSocket.settimeout(1)

# Send 10 pings to the server
for num in range(10):
    sequence_number = num + 1
    sending_time = time.time() # Time when the client sends the message
    message = 'Ping {} {}'.format(sequence_number, sending_time) # Ping message

    # Send the ping message to the server
    clientSocket.sendto(message.encode('utf-8'), (IPAddress, portNumber))

    try:
        # Receive message from the server
        response, address = clientSocket.recvfrom(1024)

        # Calculate the round trip time(RTT)
        rtt = time.time() - sending_time

        # Print the response message from the server
        print('Response message from the server: {}'.format(response.decode()))
        # Print the round trip time(RTT) in seconds
        print('RTT: {} seconds\n'.format(rtt))

    except timeout:
        print('Request timed out\n')

# Close the socket
clientSocket.close()
