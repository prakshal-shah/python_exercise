import socket

# creating socket object
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# getting host name and setting port 
host = socket.gethostname()
port = 124

# binding host to the port
socket_obj.bind((host, port))
socket_obj.listen(1)

# Establishing connection
client_socket, adr = socket_obj.accept()
while True:
    try:
        port = int(input("On what port you want to connect"))
        break
    except Exception:
        print("Enter integer only")

# Passing message to client_socket
client_socket.send(str(port).encode('utf8'))
socket_obj.close()

# creating new socket object
socket_newobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding host to the port
socket_newobj.bind((host, int(port)))
socket_newobj.listen(2)

# Establishing new connection
client_socket, adr = socket_newobj.accept()

user_input = client_socket.recv(1024).decode('ascii')
msg=""
print("You entered", user_input)
if user_input == "PING":
    msg="PING_OK"
elif user_input == "LIST":
    msg="LIST_OK"
elif user_input == "HELLO":
    msg="WORLD"
elif user_input == "QUIT":
    msg="QUIT_ERR"
else:
    msg="UNKNOWN_CMD"

# Passing message to client_socket
client_socket.send(msg.encode('ascii'))
client_socket.close()
