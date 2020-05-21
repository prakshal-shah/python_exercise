'''

Create a class for processing log statistics for attached device log files.
Constructor of this class accepts one argument which is the path to a folder containing all log files to process. 
Class should contain a method to start processing all files on demand. 
Once processing is completed, the required statistics should be loaded to class members as follows.

- num_of_errors = <integer representing number of log lines with tag "ERROR">

- num_of_warnings = <integer representing number of log lines with tag "WARNING">

- num_of_info = <integer representing number of log lines with tag "INFO">

- num_of_log_lines = <integer representing number of log lines processed for the entire operation>

All above statistics should be computed based on processing of all the log files existing in the folder. 
Make sure that computation is based on tags available in square brackets at the start of log lines and not from the message portion of log. \

i.e. Consider below fragment of log

[1071765.746 (008323):IPCDirectory:ERROR]stat services.json: No such file or directory

[1071765.746 (008323):IPCDirectory:INFO]DefaultAddress: Service ERROR 'DiscoveryService' at 'stream://localhost:40028?no_delay&nonblocking'

[1071765.746 (008323):IPCDirectory:INFO]Creation: Class WARNING at debug 'level' at 'stream://localhost:40028?no_delay&nonblocking'

Output of program:

- num_of_errors = 1

- num_of_warnings = 0

- num_of_info = 2

- num_of_log_lines = 3

Class has a print_stats method which prints the above statistics. Create instance of class and call required methods in the main program.

Attachments: 12 log*.txt files
'''
import os
import sys
class Statistics:

    def __init__(self, log_path):
        # changing path to display all log files which are in  log folder
        os.chdir(log_path)
   
    def start_logging(self):
        #Variables that stores total number of statistics
        self.total_num_of_errors=0
        self.total_num_of_warnings = 0
        self.total_num_of_info = 0
        self.total_num_of_log_lines = 0
        
        for log_files in os.listdir():
            #Print opened log file's name
            print(log_files)
            
            with open(log_files) as f:
                
                #Reading all lines of opened file
                log_file = f.readlines()
                
                #Initializing variables to zero whenever new file open
                self.num_of_errors = 0
                self.num_of_warnings = 0
                self.num_of_info = 0
                self.num_of_log_lines = 0
               
                #Reading all lines one by one from file
                for f_line in log_file:
                    
                    between_braces=f_line[f_line.find('[')+1 : f_line.find(']')]
                    
                    # if found ERROR then increases the num_of_errors counter
                    if "ERROR" in between_braces:
                        self.num_of_errors += 1
                        self.total_num_of_errors +=1
                    # if found WARNING then increases the num_of_warnings counter
                    if "WARNING" in between_braces:
                        self.num_of_warnings += 1
                        self.total_num_of_warnings += 1
                    # if found INFO then increases the num_of_info counter                    
                    if "INFO" in between_braces:
                        self.num_of_info += 1
                        self.total_num_of_info += 1
                    # Increasing line counter whenever new line read         
                    self.num_of_log_lines += 1
                    self.total_num_of_log_lines+=1
            
            # calling print_stats method to print data each time whenever file close
            self.print_stats()
        #Calling print_total_stats method to print total statistics of all log file
        self.print_total_stats()
    
    # Function that prints all counters (num_of_errors, num_of_warnings, num_of_info, num_of_log_lines)
    def print_stats(self):
        
        print("num_of_errors-", self.num_of_errors, "\nnum_of_warnings-", self.num_of_warnings,"\nnum_of_info-", self.num_of_info, "\nnum_of_log_lines-", self.num_of_log_lines, "\n")

    # Method print statistics of all log files
    def print_total_stats(self):
        print("total_num_of_errors-", self.total_num_of_errors, "\ntotal_num_of_warnings-", self.total_num_of_warnings,"\ntotal_num_of_info-", self.total_num_of_info, "\ntotal_num_of_log_lines-", self.total_num_of_log_lines, "\n")

#Store user's given path
log_path=sys.argv[1]

# creating object of class Statistics
obj=Statistics(log_path)

# Calling method of class which works on log files
obj.start_logging()