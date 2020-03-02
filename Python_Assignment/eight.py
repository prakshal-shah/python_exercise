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