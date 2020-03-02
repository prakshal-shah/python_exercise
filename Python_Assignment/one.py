"""			
													Assignment 1:
Write a simple python program which will take one string input parameter as command line argument. 
Verify if the last character of the string is Capital Letter. For e.g. If we pass “AbcD” as command line argument, 
then output should be true and for “Abcd” output would be false.
	
"""
print("Enter string")
user_input=input()
print(user_input[-1].isupper()) #print true if last character is in uppercase else print false
