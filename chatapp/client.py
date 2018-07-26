import socket
import sys
import time

#end of imports ###

#initialization section
s = socket.socket()
host = input(str("Please enter the hostname of the server: "))
port = 8080
s.connect((host, port)) #connect to the host and the given port
#if conncetion is successful,
print("Connected to chat server")
while 1:
        #piece of code that will accept the message and display it
        incoming_message = s.recv(1024) #when you type a message and press enter, it is going to be stored here.
        #we need to decode the message since we had encoded it
        incoming_message = incoming_message.decode()
        print("Server: ", incoming_message)
        print("")
        message = input(str(">>"))#for a decoded message
        message = message.encode()#to change this message into bytes since s/w interface only supports bytes 
        s.send(message)
        print("message has been sent..")
        print("")



