import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
#hee we used on of the free port
print('This is your IP address: ' ,ip)
server_host = input('Enter Friend\'s IP address: ')
name = input('Enter Friend\'s name: ')
#Here we pentert ip and nick of the second user


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(10240)
server_name = server_name.decode()

print(server_name,'has joined...')
while True:
    message = (socket_server.recv(10240)).decode()
    print(server_name, ":",message)
    message = input("Me : ")
    socket_server.send(message.encode())