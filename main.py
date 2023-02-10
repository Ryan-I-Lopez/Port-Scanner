import socket

def port_scan(host, port):
    try:
      # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # Set a timeout to avoid indefinitely waiting for a response
        sock.settimeout(10)
      # Try to connect to the target host on the target port
        result = sock.connect_ex((host, port))
      # If the connection was successful, the target port is open
        if result == 0:
            print("Port {} is open".format(port))
          # Close the socket
        sock.close()
    except:
        print("Unable to connect to host")

host = input("Enter host IP: ") # The IP address of the target host
ports = [int(x) for x in input("Enter a comma-separated list of ports to scan: ").split(",")] # The ports to scan
for port in ports: # We iterate over our target ports
    port_scan(host, port)
