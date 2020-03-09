

'''

Create a python file math.py which has three functions; sum, diff and mul.
Each function accepts two numbers. 
Function sum returns result of addition of two passed in numbers, diff returns the positive difference between two specified numbers and mul returns the multiplication of two numbers.
Numbers passed in may be integer or decimal.
Create main program python file. 
Include math.py in this main file and call three math functions.
Main program accepts two command line arguments, which are two numbers to pass into above three math functions.
Validate that specified command line parameters are integers or decimal. 
Also validate that exactly two arguments are passed to the main program from command line, if not, print the help message to pass in two numbers. 
Main program should call all three math functions over the two numbers passed in and print the output on console.
'''

import argparse
from math1 import *

#creating object of parser
parser=argparse.ArgumentParser("File program")

#check how many values are passed and that are float or not?
parser.add_argument("input", nargs=2, type=float, help="Enter integers only and only two arguments")

#parsing argument from standard input
args=parser.parse_args()

#assigning command line values to num1 and num2
num1,num2=args.input[0:2]

#calling all functions of math1 file
print("Addition is: ",add(num1,num2))
print("Multiplication is: ",mul(num1,num2))
print("Difference is: ",diff(num1,num2))	