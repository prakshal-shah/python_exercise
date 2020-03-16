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
import sys
from socket import gethostbyname
   
def conn_client(client_socket):
            
    try: 
        while True: 
               
            user_input = client_socket.recv(1024).decode('ascii')
            #if and else if to find match with predefined commands
            if user_input == "PING":
                msg = "PING_OK"
               
            elif user_input == "LIST":
                msg = "LIST_OK"
                
            elif user_input == "HELLO":
                msg = "WORLD"
               
            elif user_input == "QUIT":
                msg = "QUIT_ERR"
              
            else:
                msg = "UNKNOWN_CMD"
                
            # Passing message to client_socket
            client_socket.send(msg.encode('ascii'))
            user_choice = client_socket.recv(1024).decode('ascii')
            if user_choice == "yes" or user_choice == "YES":
                print("")
                # Checking commands with user entered command
            else:
                # Closing client-socket
                client_socket.close()
                        
    except :
        print("")        

# creating socket object
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
# getting host name and setting port 
host = socket.gethostname()
port = 200
            
try:
    #Taking input from command line argument and assigning values to host and port
    host = sys.argv[1]
    port = sys.argv[2]
except:
    print("no external port or host passed in command line argument")
            
# binding host to the port
try:
    socket_obj.bind((host, int(port)))
    print("server IP is:",gethostbyname(host),"Port is:",port)
except socket.gaierror:#If user enter wrong IPaddress
    print("Wrong IPaddress")
except:
    print("Error while connecting")            

while True:  
    socket_obj.listen(2)
    # Establishing connection
    client_socket, adr = socket_obj.accept()    
    obj = conn_client(client_socket)
    
socket_obj.close()
