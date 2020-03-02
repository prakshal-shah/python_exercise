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

class Statistics:
    
    def __init__(self, log_path):
        # changing path to display all log files which are in  log folder
        os.chdir(log_path)
   
    def start_logging(self):
        for log_files in os.listdir():
            print(log_files)
            
			# opens all log files one by one
            with open(log_files) as f:
                f = f.readlines()
               
			    # set error, warnings, info, line to zero everytime when new file opens
                num_of_errors = 0
                num_of_warnings = 0
                num_of_info = 0
                num_of_log_lines = 0
                for x in f:
                   
				   # if found ERROR then increases the num_of_errors counter
                    if "ERROR" in x:
                        num_of_errors += 1

                    # if found WARNING then increases the num_of_warnings counter
                    if "WARNING" in x:
                        num_of_warnings += 1
                    
                    # if found INFO then increases the num_of_info counter                    
                    if "INFO" in x:
                        num_of_info += 1
                   
				   # Increasing line counter whenever new line read         
                    num_of_log_lines += 1
           
		    # calling print_stats function with passing all counters
            print_stats(num_of_errors, num_of_warnings, num_of_info, num_of_log_lines)

# Function that prints all counters (num_of_errors, num_of_warnings, num_of_info, num_of_log_lines)
def print_stats(num_of_errors1, num_of_warnings1, num_of_info1, num_of_log_lines1):
        
    print("num_of_errors-", num_of_errors1, "\nnum_of_warnings-", num_of_warnings1,
          "\nnum_of_info-", num_of_info1, "\nnum_of_log_lines-", num_of_log_lines1, "\n")


# creating object of class Statistics
a = Statistics(r"C:\Users\prakshal.shah\eclipse-workspace\first\log_files")
# Calling method of class which works on log files
a.start_logging()
