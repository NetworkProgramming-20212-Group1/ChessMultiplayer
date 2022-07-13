import socket
import threading
from datetime import datetime

response = []
host = '127.0.0.1'
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

def getRequest():
    while True:
        data = s.recv(1024).decode('ascii')
        response.append(data)
        with open('server_response.txt', 'a') as f:
            output = '['+datetime.now().strftime("%H:%M:%S")+']: '+data
            f.write(output)

def sendRequest():
    while True:
        message = input("Enter your value: ")
        if message=="close":
            s.close()
        message+='\n'
        s.send(message.encode('ascii'))

def handleResponse():
    while True:
        print(response)
        # xu li request ma server chu dong gui ve


def Main():
    try:
        t1 = threading.Thread(target=getRequest, args=())
        t2 = threading.Thread(target=sendRequest, args=())
        t2.start()
        t1.start()
        t1.join()
        t2.join()
    except:
        print ("error")

if __name__ == '__main__':
    Main()