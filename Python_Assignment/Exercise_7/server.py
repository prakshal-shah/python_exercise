'''

    Create a simple client-server socket based command processing application. 
	There are two python files, one is server and other is client.
	Python server is listening on some port on local machine and waiting for client connection.
	Multiple client instances can make connection to the server.
	Upon starting server, it should print on what port and IP it is listening on.
	Default server port is defined inside server script and it can be overridden by passing command line parameter while starting server.
	Client should accept server info as command-line parameters.
	Upon connecting to server, client will print connected to server message.
	Client then waits for user to input a command string. 
	This command string is then passed to server for processing and whatever server returns in response should be printed on client std-out.
	Implement below command->response messages at server side. 
	Proper exception handing should be made while establishing client-server connection.

  COMMAND         | RESPONSE

-------------------------------

  PING            | PING_OK

  LIST            | LIST_OK

  HELLO           | WORLD

  QUIT            | QUIT_ERR

  <anything else> | UNKNOWN_CMD

'''
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
