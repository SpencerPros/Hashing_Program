## Name: Spencer Prosniewski
## Purpose of Program: Network Port Scanner

import socket

def port_scan(target, start_port, end_port):
    # Iterate through the range of ports to scan
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target, port))
        
        # Check if the connection was successful (port is open)
        if result == 0:
            print(f"Port {port} is open")
        
        # Close the socket connection
        sock.close()

# Example usage
# Get the target IP address from user input
target_ip = input("Enter the target IP address: ")

# Get the starting and ending port numbers from user input
start_port_number = int(input("Enter the starting port number: "))
end_port_number = int(input("Enter the ending port number: "))

# Call the port_scan function with user-provided inputs
port_scan(target_ip, start_port_number, end_port_number)