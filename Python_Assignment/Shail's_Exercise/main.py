"""
User enter the details of table to perform CRUD operations.
The main.py get only user input and calling the methods of another class Methods are for,
creating table, insert into table, Update table, Delete row, Delete/Drop Table, Print all data of a table.
Firstly when file run it should ask user to which database file he/she want to perform all operations, if that database dosen't exists then the con structor should make new database file.
Another file cosists only Methods.

"""

from pip._vendor.msgpack.fallback import xrange
from operations import sql_operations
import sqlite3

# Object of another file to call that functions
sql_obj = sql_operations()

# Ask user if he/she wants to perform any operation
while True:  
   
    # Variable to store user's choice
    user_ask = 0  
    try: 
        user_ask = int(input("1: Create table \n2: Insert into already exists table and exit \n3: Update table \n4: Delete row \n5: Delete whole table \n6: Print table data \n7: Close database"))        
    except:
        print("Enter integer values only")

    # If user want to create table
    if user_ask == 1:
        tb_args = []
        tb_type = []
        # getting table details
        new_tb_name = input("Enter table name:")
        while True:    
            try:
                tb_no_args = int(input("how many columns you want to enter"))
                break   
            except:
                print("Enter integer values only")
        for i in xrange(tb_no_args):
            tb_args.append(input("Enter columns and it's type separated with single white space"))
        
        # Calling function of another file to create table
        sql_obj.create_tb(new_tb_name, tb_args)
        # Clearing details if user need to create many tables at a time
        tb_no_args = ""
        tb_args = []
  
    # If user want to insert into table
    if user_ask == 2:
        data_insrt = []
        # Ask user that how many data he/she want to enter
        while True:    
            try:
                no_data_insrt = 1
                tb_name = input("Enter table name:")
                # Printing table data for user 
                sql_obj.sql_printit(tb_name)
                no_data_insrt = int(input("How many row you want to insert?"))

                break
            except sqlite3.OperationalError:
                print("Enter valid table name")
        
            except ValueError:
                print("Enter integer values only")
      
        # Getting columns name of given table 
        tb_args = sql_obj.get_column()
        
        # user inserts values of table
        for i in xrange(no_data_insrt):
            for j in tb_args:
                print(f"Enter data of {j}")
                data_insrt.append(input())
                
            # Calling function of another file to insert values
            sql_obj.insert_values(tb_name, data_insrt)
            data_insrt = []

    # If user want to update table
    if user_ask == 3:
        while True:  
            try:
                # Getting all information from user required to update table
                tb_name = input("Insert into (write table name)")
                tb_column = input("SET (enter col_name)")
                new_data = input("= (new value) ")
                tb_column1 = input("WHERE (col_name)")
                old_data = input("=(that col_data)")
                # Calling function of another table to update table
                sql_obj.sql_update(tb_name, tb_column, tb_column1, old_data, new_data)
                break
            except:
                print("Update failed")
  
    # If user want to delete row
    if user_ask == 4:
        while True:
            try:
            # Getting info required to delete a particular row
                tb_name = input("In which table you want to delete row")
                tb_column = input("From which column you want to delete")
                old_data = input("Write data which you want to delete")
                sql_operator = input("Enter one operator like (==,>,<,>=,<=)")
                sql_obj.sql_del_row(tb_name, tb_column, sql_operator, old_data)
                break
            except:
                print("Delete operation failed")
  
    # If user want to drop table
    if user_ask == 5:
        while True:
            try:
                # Asks user to write table name which he/she want to delete
                tb_name = input("Which table you want to delete")
                # Calling function of another file to drop table
                sql_obj.delte_tb(tb_name)
                print("Table dropped or deleted")
                break
            except:
                print("Drop operation failed")
   
    # If user want to print table data
    if user_ask == 6:
        while True:
            try:
                tb_name = input("Enter table name:")
                # Calling function of another file to print all data of a table
                sql_obj.sql_printit(tb_name)
                break
            except:
                print("Enter table name again")
  
    # close open database
    if user_ask == 7:
        # calling function to close connection
        sql_obj.db_close()