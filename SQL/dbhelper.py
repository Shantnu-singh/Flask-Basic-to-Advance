import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost" , username = "root" , password = "" , database = "employees")
            self.mycursor = self.conn.cursor()
        except:
            print("Connected to the database")
        
        else:
            print("Coudn't connect to th Database")
            
    def register(self , name , email , password):
        try:  
            self.mycursor.execute(""" 
                            INSERT INTO 'users' ("id" , "name" , "email" , "password") VALUES (NULL, '{}' , '{}', '{}' , '{}')
                                """.format(name , email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
    def login(self , email , password):
            self.mycursor.execute("""
                                  SELECT * FROM users WHERE email LIKE {} AND password LIKE {} """.format(email , password))
            return self.mycursor.fetchall()
 
        
        