#SERVER CODE
import socket

print("WELCOME TO THE TCP SERVER")
#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the docket to a specific address and port
server_address = ('172.17.0.2', 32840)
sock.bind(server_address)

#listen for incoming connections
sock.listen(1)

def process_data( xdat):
#    print("RX BY SERVER: ", xdat)
    return(xdat+ b' ==> PROCESSED BY SERVER')

print("Entering Listening Mode ....")
while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        #Receive the date form the client
        data = connection.recv(1024)
        sdata = data.decode('utf-8')
        #Process the Data
        result = process_data(data)
        
        #Send the result back to the CLient
        print(client_address,"[" , f"{len(sdata):04d}", "] : ", sdata)

#        print("TX to CLIENT: ", result)
        connection.sendall(result)

    finally:
        #Clean up the connection
        connection.close()

