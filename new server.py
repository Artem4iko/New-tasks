from encodings import utf_8
import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP :", s_ip)
#Here can see host ip addres

name = input('Enter name: ')
#Here need to print our nick

new_socket.listen(2)


conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established.Connected From: ',add[0])

#Here we see the response about the connection status
 
client = (conn.recv(10240)).decode()
print(client +'has connected. ')

conn.send(name.encode())
while True:
    message = input('Me: ')
    conn.send(message.encode())
    message = conn.recv(10240)
    message = message.decode()
    print(client, ':',message)
    