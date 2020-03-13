import socket
import sys

try:
    # creating socket object
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting host and port
    host = socket.gethostname()
    port = 200
    
    try:
        #Setting host and port values given by user in command line argument
        host= sys.argv[1]
        port=sys.argv[2]
    except:
        print("no external port or host passed in command line argument")
  
    # Connecting the host on port
    try:
                socket_obj.connect((host, int(port)))
                print("Connected to server")

    except socket.gaierror:#gaierror is for, if user enters wrong IP address
                print("Wrong IPaddress")
    except:
                print("Error while connecting")
    
    while True: 
        
        user_input = input("\nEnter any one command at a time \nCommands are:\tPING  LIST  HELLO  QUIT")
        socket_obj.send(user_input.encode('ascii'))
       
        # Storing message which is sent from server
        msg = socket_obj.recv(1024).decode('ascii')
        # Printing message which is passed by another file on socket
        sys.stdout.write(msg)
        user_ask=input("\nDo you want to enter again??\nYES to Continue")
        if user_ask == "yes" or user_ask == "YES":
            socket_obj.send(user_ask.encode('ascii'))
        else:
            break
    # Close the connection
    socket_obj.close()
except:
    print("Unknown error occured")