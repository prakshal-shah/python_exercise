"""
										Assignment 4:
Write a function which accepts an int count of a number of items. Function returns a string such that:
'Number of items: <count>', where <count> is the number passed in.
However, if the count is 10 or more, then use the word 'many' instead of the actual count.
i.e. function(4) returns 'Number of items: 4'
and function(21) returns 'Number of items: many'
"""
#Function for count it returns many or the number itself
def count_int(user_input):

    if(user_input>=10):
       return "many"
    else:
        return user_input
#getting user input
while True:
    try:
        user_input=int(input("Enter number of items"))
        break
    except ValueError:
        print("Enter integers only")

#calling the method count_int and passing the user entered value to that function
message=count_int(user_input)

#printing the function's returned value 
print("Number of items : ",message)    