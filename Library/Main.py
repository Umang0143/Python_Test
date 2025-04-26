import json
import os
import datetime

path=fr"D:\Indixpert 2025\Python_Test\Library\Bookslist.json"
log=fr"D:\Indixpert 2025\Python_Test\Library\logs.txt"

class Library:
    def __init__(self):
        self.__pin=1995
        self.books=[]
        self.load_books()
    
    def writelogs(self,logs):
        with open(log, "a") as file:
            file.write(logs + "\n")
            
    def verify_pin(self):
        try:
            pin = int(input("Enter your PIN: "))
            return pin == self.__pin
        except Exception as e:
            print("PIN must be a number.")
            data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            logs=json.dumps(data,indent=4)
            self.writelogs(logs)
    
    def load_books(self):
        if os.path.exists(path):
            with open(path, "r") as file:
                self.books = json.load(file)
        else:
            self.books = []
    
    def save_books(self):
        with open(path, "w") as file:
            json.dump(self.books, file, indent=4)

    def menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Books")
            print("2. Borrow Books")
            print("3. Return Books")
            print("4. Books Details")
            print("0. Exit")
            print("*" * 20)
            try:
                choice=int(input("Enter your choice (0 to 4):- "))
            except Exception as e:
                print("\nInvalid input! please enter a number.")
                data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs=json.dumps(data,indent=4)
                self.writelogs(logs)
                continue

            if choice == 0:
                print("Exit...")
                break
            elif choice == 1:
                add=Add_Books()
                add.load_books()
                add.add_books()
            elif choice == 2:
                borrow=Borrow_Books()
                borrow.borrow_books()
            elif choice == 3:
                Return=Return_Books()
                Return.return_books()
            elif choice == 4:
                details=Books_Alldetails()
                details.all_details()
            else:
                print("\nInvalid Choice! Please select from (0 to 4).")

class Add_Books(Library):
    def add_books(self):
        if self.verify_pin():
            name={}
            name["book"]=input("enter your add book name:- ")
            self.books.append(name)
            self.save_books()
            print(f"\nBook '{name['book']}' added successfully.\n")  
        else:
            print("Wrong PIN!")

class Borrow_Books(Library):
    def borrow_books(self):
        self.load_books()
        if self.verify_pin():
            name=input("Enter your borrow book name:-")
            found=False
            for listdata in self.books:
                for key,value in listdata.items():
                    if value.lower() == name.lower():
                        self.books.remove(listdata)
                        self.save_books()
                        print(f"\nBook '{name}' borrowed successfully.")
                        found=True
                        break
            if not found:
                print(f"\nBook '{name}' not found.")
        else:
            print("Wrong PIN!")

class Return_Books(Library):
    def return_books(self):
        self.load_books()
        if self.verify_pin():
            name=input("Enter your return book name:- ")
            book={"book": name}
            self.books.append(book)
            self.save_books()
            print(f"\nBook '{name}' returned successfully.")
        else:
            print("Wrong PIN!")

class Books_Alldetails(Library):
    def all_details(self):
        try:
            if os.path.exists(path):
                with open(path, "r") as file:
                    print("\n--- List of Available Books ---")
                    print(file.read())
            else:
                print("\nNo books file found.")
        except Exception as e:
            print("Error reading books file.")
            data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            logs=json.dumps(data,indent=4)
            self.writelogs(logs)

data=Books_Alldetails()
data.menu()