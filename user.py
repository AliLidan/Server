import socket

socket_server = socket.socket()

name = input("")
socket_server.connect(("127.0.0.1", 50))
socket_server.send((name.encode("utf-8")))
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print("Пользователь "+name+" присоединился к "+server_name)

while True:
    message = socket_server.recv(1024).decode()
    print(server_name, " : ", message)
    message = input(name+": ")
    socket_server.send(message.encode())