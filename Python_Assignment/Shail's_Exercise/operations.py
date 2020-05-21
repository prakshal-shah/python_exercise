import sqlite3

class sql_operations:
    
    # Constructor for connection to database  
    def __init__(self):
        db1 = input("Enter database file name")
        self.db = sqlite3.connect(db1)
        self.cur = self.db.cursor()
    
    # Function to add new table in database
    def create_tb(self, tb_name, tb_args):
        
        sql = f'CREATE TABLE {tb_name} (' + ','.join(tb_args) + ')'
        print(sql)
        
        try:
            self.cur.execute(sql)
            print("created")
            tb_args = []
            tb_name = ""
        except:
            print("not created")
        self.db.commit()
   
    def get_column(self):
   
        column_names = [i[0] for i in self.cur.description]
        return column_names   
   
    # Function to add data in table   
    def insert_values(self, tb_name, data_insrt):

            res = str(data_insrt) [1:-1]
            f = f"INSERT INTO {tb_name} VALUES ({res})"
            print(f)
            try:
                self.cur.execute(f)
            except:
                print("not inserted")
#             self.db.commit()
        
    # Function for updating database
    def sql_update(self, tb_name, tb_column, tb1_column, old_data, new_data):  

        sql_qry = f"UPDATE {tb_name} SET {tb_column} = '{new_data}'\
         WHERE {tb1_column}='{old_data}' "
        print(sql_qry)
        
        self.cur.execute(sql_qry)
        self.db.commit()

    # Function to delete column from table        
    def sql_del_row(self, tb_name, tb_column, sql_operator, old_data):    
        
        sql = f"DELETE FROM {tb_name} WHERE {tb_column} {sql_operator} '{old_data}'"
        print(sql)
        self.cur.execute(sql)
        self.db.commit()
    
    # Function to remove table from database  
    def delte_tb(self, tb_name):
      
        sql = f"DROP TABLE {tb_name}"
        print(sql)
        self.cur.execute(sql)
        self.db.commit()
   
    # Function to print table data database  
    def sql_printit(self, tb_name):
        
        sql = f"SELECT * FROM {tb_name}"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        column_names = [i[0] for i in self.cur.description]        
        
        # Printing column names
        print("TABLE:\n", column_names)
        # Printing table rows
        for i in data:
            print(f"{i}\t")
           
        self.db.commit()
    
    # Function for closing connection of database
    def db_close(self):
        
        self.db.close()
        print("Database connection closed")
