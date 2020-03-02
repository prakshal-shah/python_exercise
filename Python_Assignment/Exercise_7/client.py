import socket

# creating socket object
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Setting host and port
host = socket.gethostname()
port = 124

# Connecting the host on port
socket_obj.connect((host, port))
# Storing message which is sent from server
msg = socket_obj.recv(1024).decode('utf8')

# Converting that string to integer
port_num = int(msg)
# Close the connection
socket_obj.close()

# creating new socket object
socket_newobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the host on port
socket_newobj.connect((host, port_num))
 
print("Connection established")
user_input = input("Enter any one command at a time \nCommands are:\tPING  LIST  HELLO  QUIT")
socket_newobj.send(user_input.encode('ascii'))
    
# Storing message which is sent from server
msg = socket_newobj.recv(1024)
    
# Printing message which is passed by another file on socket
print(msg.decode('ascii'))
   
# Close the connection
socket_newobj.close()