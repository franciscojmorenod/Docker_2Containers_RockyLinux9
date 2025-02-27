
#CLIENT CODE
import socket
import argparse
print("WELCOME TO THE TCP  CLIENT")

#===============================================================

parser = argparse.ArgumentParser(description='Usage: TCPserver ipaddress port')
parser.add_argument('-i', '--ipaddress', type=str, default='172.17.0.2', help='Server IP address')
parser.add_argument('-p', '--port', type=int, default = 2022, help='Port Number')

args = parser.parse_args()

ServerIPaddress = args.ipaddress
ServerPort = args.port

print( "Server Address =", ServerIPaddress)
print( "Server Port    =", ServerPort)

#===============================================================

while(True):


#print ("Sending Data")
    try:
        #Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Bind the docket to a specific address and port
        server_address = (ServerIPaddress, ServerPort)
        sock.connect(server_address)

        # send some data to the server
        indata = input(">")
        yu = len(indata)
        data = str.encode(indata)
        sock.sendall(data)

        # Receive the response form the Server
        result = sock.recv(1024)
        print("\033["+ str(yu) + "C\033[1A : ACKed", yu)
    finally:
        # Clean up to the socket
#        print("Sent")
#        print("Closing socket")
        sock.close()
    

