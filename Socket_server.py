
# first of all import the socket library 
import socket                
  
# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
print ("socket binded to %s" %(port))
s.bind(('', port))
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")

print('Waiting for connection...')
c, addr = s.accept()      
print ('Got connection from', addr)
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
   # Establish connection with client. 
   receivedMsg=c.recv(1024).decode()
   print (receivedMsg)
   if (receivedMsg=='disconnect'):
      break
 
   # send a thank you message to the client.  
   st="Messgage"
   byt=st.encode()              #this is require in python 3
   c.send(byt) 
  
# Close the connection with the client 
c.close() 
