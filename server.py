import socket

new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 2))
new_socket.listen(5)

print("Сервер запущен")
name = input("Введите ваше имя:")
connection, address = new_socket.accept()

print("Пользователь " + name + "присоединился")

connection.send(name.encode("utf-8"))

while True:
    message = connection.recv(1024).decode()
    print(name + " : " + message)
    message = input(name + ": ")
    connection.send(message.encode())

