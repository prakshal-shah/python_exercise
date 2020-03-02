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

import math1
while True:
    try:
        num = int(input("Enter 1st number"))
        num1 = int(input("Enter 2nd number\n"))
        break
    except ValueError:
        print("Enter integer only and also pass both number because null is not valid\n")
# calling the add function of the math1 file
print("Addition of %d and %d are" % (num, num1), math1.add(num, num1)) 

# calling the mul function of the math1 file
print("Multiplication of %d and %d are" % (num, num1), math1.mul(num, num1)) 

# calling the diff function of the math1 file
print("Difference between %d and %d are" % (num, num1), math1.diff(num, num1), "+ve differnce")  

