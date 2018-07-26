import socket #helps us do stuff related to networking
import sys
import time

#end of imports ###

#initialization section

s = socket.socket()
host = socket.gethostname() #gets the local hostname of the device
print("Server will start on host:", host) #gets the name of my desktop/host of the whole connection(when I run the program)
port = 8080 #make sure the port is on my local host(my computer)
s.bind((host,port)) #binds the socket with the host and the port
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
#we can now start listening to incoming connections
s.listen(1) #we accept only one connection
conn,addr = s.accept()
print("")
#conn is assigned to the socket itself which is the physical socket (s?) coming from the client
#addr is assigned to the IP address of the client that we'll be connecting
print(addr, "Has connected to the server and is now online...") #prints the IP Address/Hostname of the client that is connected to us
print("")

#now move on to the client side.
#we're back!

while 1:
        message = input(str(">>"))#for a decoded message
        message = message.encode()#to change this message into bytes since s/w interface only supports bytes 
        conn.send(message)#conn is the client that is connected to us
        print("message has been sent..")
        print("")
        #piece of code that will accept the message and display it
        incoming_message = conn.recv(1024) #when you type a message and press enter, it is going to be stored here.
        #we need to decode the message since we had encoded it
        incoming_message = incoming_message.decode()
        print("Server: ", incoming_message)
        print("")
        

#so far we have a one-sided chat
#we need to therefore put it in a loop
