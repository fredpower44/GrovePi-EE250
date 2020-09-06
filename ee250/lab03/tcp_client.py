"""
Server IP is 52.88.20.156, ports are 5000-5008, socket is UNIX TCP 
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""

#Name: Frederick Zhang
#Github link: https://Github.com/fredpower44/GrovePi-EE250.git


import socket

def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("52.11.228.142", 5000))
    # TODO: Get user input and send it to the server using your TCP socket
    msg = input("Enter a message to be sent\n")
    s.sendall(bytes(msg, "utf-8"))

    # TODO: Receive a response from the server and close the TCP connection
    data = s.recv(1024)
    s.close()

    print(data.decode("utf-8"))

if __name__ == '__main__':
    main()
