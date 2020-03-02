

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

import sys
import argparse
from math1 import *

#creating object of parser
parser=argparse.ArgumentParser("File program")
#check how many values are passed and that are integers or not?
parser.add_argument("add", nargs=2, metavar="enter 2 numbers only", type=int, help="Enter integers only and only two arguments")
#parsing argument from standard input
args=parser.parse_args()

#assigning command line values to a and b
num1,num2=args.add[0:2]
#calling all functions of math1 file
print(add(num1,num2))
print(mul(num1,num2))
print(diff(num1,num2))