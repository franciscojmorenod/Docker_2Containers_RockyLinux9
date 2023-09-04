
#CLIENT CODE
import socket

print("WELCOME TO THE TCP  CLIENT")

while(True):


#print ("Sending Data")
    try:
        #Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Bind the docket to a specific address and port
        server_address = ('172.17.0.2', 32840)
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
    

