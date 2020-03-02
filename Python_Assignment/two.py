"""
													Exercise: 2
     Consider the following lists:

Index_list = [1,2,3,4,5,6,7,8,9,10,11,12]

Name_list = [‘Jan’, ‘Feb’, ‘Mar’, ‘Apr’, ‘May’, ‘Jun’, ‘Jul’, ‘Aug’, ‘Sep’, ‘Oct’, ‘Nov’, ‘Dec’]

a.  Create a dictionary with the above lists such that index_list is key and name_list is value.

For e.g. {1:’Jan’, 2:’Feb’} and so on ….

Now take an input number from user, validate it is between 1 and 12. 
Using above dictionary print the corresponding month name for the user input number.

b. Create a list of tuples with the above lists as shown below:

[(1,’Jan’), (2,’Feb’), (3,’Mar’)] and so on…

Now iterate through each tuple from above list and store them to a CSV file (month_names.csv) like below:

id, month_num, month_name

0, 1, Jan

1, 2, Feb

…

11, 12, Dec													
"""



# A's Implementation

import csv
Index_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
name_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthdict = {}

#for loop to store index list as key and month list as value
for i in range(0, len(Index_list)):
    monthdict[Index_list[i]] = name_list[i]
print(monthdict)

#Getting user input 
while True:
    try:
        getname = int(input("Enter a number between 1 to 12 to view month name"))
        break;
    except Exception:
        print("Enter integers only and also don't include white spaces\n")
    
#condition checks and print appropriate value if given number not found and print not found
if monthdict.get(getname) != None:
    print(monthdict[getname],"\n")
else:
    print("not found\n")


#  B's Implementation 

monthlist = list(monthdict.items())
print(monthlist)
monthlist_for_csv = [(index1, k, v) for index1, (k, v) in enumerate(monthlist)]
#storing list in csv file
with open ("months.csv", "w", newline="") as csfile:
    
    write = csv.writer(csfile)
    write.writerow(['INDEX', 'MONTH NUMBER', 'MONTH NAME'])
    write.writerows(monthlist_for_csv)
    
#printing the csv file to view output
with open ("months.csv", "r") as csfile1:

    read = csv.reader(csfile1)
    write_count = 0
    for rows in read:
        if write_count == 0:
            print('\n\t\t\t COLOUMN NAME\n')
            print(f' \t\t{"    ".join(rows)}')
            write_count += 1
        else:
            print(f'\t\t  {rows[0]}\t\t{rows[1]}\t    {rows[2]}')