## Objective: 
The objective is:  
    - to create an image with the Linux Rocky9 OS.  
    - to create a Multi-Container System (2 containers in this case).  
    - to test how the two containers can communicate in a network via TCP sockets.  
    - to create each container using the same image.  
    - to use Docker to perform this work.  

## Procedure
- Run fm2.bat to create the image and containers
    - Build a Docker image using rockylinux:9
    - Create 2 Containers using the just created image
    - Run the containers

- Refer to the "Dockerfile" for the more details


## Running the TCPserver    
- From a terminal Connect to the container1 by doing:  
    docker exec -it container1ID /bin/bash  
    get the ipaddress by typing : ifconfig  

    run the TCP server by typing  
    - $ python3 TCPserver.py
        - WELCOME TO THE TCP SERVER
        - Server Address = 172.17.0.2
        - Server Port    = 2022
        - Entering Listening Mode .... 
## Running the TCPclient  
- From a different terminal Connect to the container1 by doing:  
    $ docker exec -it container2ID /bin/bash    
    get the ipaddress by typing : ifconfig  

    run the TCP client by typing  
    - $ python3 TCPclient.py
        - WELCOME TO THE TCP  CLIENT
        - Client Address = 172.17.0.3
        - Client Port    = 2022

    - Type your message at the client's prompt and verify that the exact message is captured and displayed at the servers end.


# Needed tools install by the Dockerfile:
    RUN dnf -y install net-tools
    RUN dnf -y install openssh-server
    RUN dnf -y install pip
    RUN dnf -y install iputils
    RUN dnf -y install nano
    RUN pip3 install requests
    RUN pip3 install netifaces

# The image contains the following python programs:
    - hello.py        : Test program that exercises various tools  
    - TCPserver.py    : Run this from Container1  
                        Program enters capture mode and waits for messages from the  TCPclient  
    - TCPclient.py    : Run this from Container2.  
                        User can send messages to the server over a TCP socket.  
                        Message is captured and displayed by the TCPserver   


