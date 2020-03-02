'''
Create a thread class of which run method print numbers in sequence with a delay of n seconds.
Number starts with 0. It prints number prefixed with thread name.
Now create three thread instances one with 1 second delay, other with 1.5 seconds delay and third with 2 seconds delay.
Start each thread in the main program. 
Upon running python file it should start all these threads and also it should expect a integer from user as input. 
If user inputs 0 it should terminate all these three threads and terminate the program. 
For any other input it does nothing.

'''
import threading
import time

#active variable to handle while loop
active=True

#Thread class having method run
class threads(threading.Thread):
    
    def __init__(self,thread_name,delay):
        
        threading.Thread.__init__(self)
        self.name=thread_name
        self.delay=delay
    
    def run(self):
        
        count=0
        while active:
            time.sleep(self.delay)
            #Print thread name and counter value
            print(self.name,"\t",count,"\n")
            count+=1

#Function that gets user input     
def wait_on_user():

    global active
    while True:
        #try used because user can enter non integer value
        try:
            #Getting user input
            user_interrupt = int(input())
            #If user enters zero then program will terminate
            if user_interrupt==0:
                #set active to false to stop the while loop
                active=False
                break
        except:
            print("")
   
Thread1=threads("Thread-1",1)
Thread2=threads("Thread-2",1.5)
Thread3=threads("Thread-3",2)
#It calls the wait_on_user method 
Thread4 =threading.Thread(target=wait_on_user)

#Starting all threads one by one
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()