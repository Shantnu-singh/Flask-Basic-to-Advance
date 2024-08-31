from dbhelper import DBhelper
import sys

class flipart:
    def __init__(self):
        self.Db_obj = DBhelper()
        self.menu()
        
    def menu(self):
        choice = input("""
              1. Enter 1 to register
              2. Enter 2 to login
              3. Anything Else to leave""")
        
        if choice == "1":
            pass
            self.register()
        elif choice == "2":
            pass
            self.login()
        else:
            sys.exit(100)
    
    def register(self):
            name = input("Enter the name:\n")
            email = input("Enter the email:\n")
            password = input("Enter the password:\n")
            
            responce = self.Db_obj.register(name , email , password) 
            
            if responce == 1:
                print("Registraction sucessful !!!")
            else :
                print("registration failed..... try again ")
    
    def login(self):
            email = input("Enter the email:\n")
            password = input("Enter the password:\n")
            data = self.Db_obj.login(email , password)
            
            if data == -1:
                print("Error loding in the data")
            else:
                print(data)
                
            
obj = flipart()