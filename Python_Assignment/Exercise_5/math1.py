'''
Validate that specified command line parameters are
 integers or decimal. Also validate that exactly two 
 arguments are passed to the main program from command 
 line, 
 if not, print the help message to pass in two 
 numbers. Main program should call all three math 
 functions over the two numbers passed in and print 
 the output on console.
'''


# Function adds two number and return its sum
def add(num1, num2):
    return num1 + num2


# Function multiplies two number and return answer
def mul(num1, num2):
    return num1 * num2


# Function finds difference between two number and return difference
def diff(num1, num2):
    return(abs(num1 - num2))
