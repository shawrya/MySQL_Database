import mysql.connector


class Mysql_database:
    def __init__(self):
        '''
        The connection is initalized in the init method
        so the connnection will be done as the object of the class is initalize
        '''

        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = 'pythondatabase',
        charset='utf8')
        print(self.mydb)

    def create_database(self):
        '''
        This function will create a scheme in the database
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("create database pythondatabase") # instead of mydatabase you can write any name that you want
        print('Database created')

    def show_databases(self):
        '''
        this function is used to show all the databases in your system
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute('show databases')
        for _ in mycursor:
            print(_)

    def create_table(self):
        '''
        This function is used to create table
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE TABLE customers (name VARCHAR(20), address VARCHAR(255))")
        print('table created')

    def show_tables(self):
        '''
        This function is used to show tables
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for _ in mycursor:
          print(_)

    def alter_table(self):
        '''
        This function is used to alter table
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        print('table altered')

    def insert_into_table(self):
        '''
        this function is used to insert values in tables
        TO input the multiple values in database put the values in list format
        like this [(values1),(values2)]
        '''
        mycursor = self.mydb.cursor()
        sql_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        values = ("Pratik", "somewhere on earth")
        mycursor.execute(sql_query, values)
        self.mydb.commit() #It is required to make the changes, otherwise no changes are made to the table.
        print(mycursor.rowcount, "record inserted.")


    def select_query(self):
        '''
        This function is used to select all the values in the table
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM customers") #the select statment can be alter as per the need
        myresult = mycursor.fetchall() #Here all the values will be fetch using fetchall to fetch one value use fetchone()
        for _ in myresult:
          print(_)

    def delete_query(self):
        '''
        This function is used to delete values
        '''
        mycursor = self.mydb.cursor()
        sql_statement = "DELETE FROM customers WHERE address = 'somewhere on earth'"
        mycursor.execute(sql_statement)
        self.mydb.commit() #It is required to make the changes, otherwise no changes are made to the table.
        print(mycursor.rowcount, "record(s) deleted")


    def drop_table(self):
        '''
        This function is used to drop a table
        '''
        mycursor = self.mydb.cursor()
        sql_statement = "DROP TABLE IF EXISTS customers"
        mycursor.execute(sql_statement)

    def update_table(self):
        '''
        This function is used to update table
        '''
        mycursor = self.mydb.cursor()
        sql_statement = "UPDATE customers SET address = 'los angles' WHERE address = 'las vegas'"
        mycursor.execute(sql_statement)
        self.mydb.commit()  #It is required to make the changes, otherwise no changes are made to the table.




if __name__ =="__main__":
    md = Mysql_database()
    md.create_database() # crete database
    md.show_databases() #show all the databases
    md.create_table() # create tables
    md.show_tables() # show all the bales in the database
    md.alter_table() # alter table
    md.insert_into_table() # insert into table
    md.select_query() #select query
    md.delete_query() #delete  a value / values in table
    md.drop_table() # drop tables
    md.update_table() #update values in table
