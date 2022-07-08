
# Import socket module
import socket
global int
 
def Main():
    # local host IP '127.0.0.1'
    host = '172.29.126.246'
 
    # Define the port on which you want to connect
    port = 1234
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    s.connect((host,port))
 
    # message you send to server
    while True:
        
        message = input("Enter your value: ")
        
        if message=="close":
            s.close()


        message+='\n'

        

        s.send(message.encode('ascii'))
 
        # message received from server
        data = s.recv(1024).decode('ascii')
        # handle response from server
 
        # print the received message
        print('Received from the server :'+data)
 
     
    # close the connection
 
if __name__ == '__main__':
    Main()