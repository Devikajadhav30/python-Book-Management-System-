# Python Pre-Django Task: Book Management System  
"""Task Description  

Create a Python program that:  

1. Adds books: Specify a book title and quantity to add.  

2. Removes books: Decrease the quantity of a book and delete it if the quantity reaches zero.  

3. Views book collection: Show a list of books and their quantities.  

4. Gets total books: Display the total number of books currently available.  

All functionality must be encapsulated within a class. The class should include methods to handle each of these operations.  

Requirements  
1. Use a class structure:  

   - Create a `BookCollection` class.  

   - The class should contain methods for adding, removing, viewing, and getting total book count.  

2. Handle invalid inputs:  

   - Ensure valid book titles and quantities.  

   - Prevent removing more books than available.  
3. Use appropriate data structures:  

   - A dictionary should be used inside the class to maintain book quantities.  

Example Program Flow  

1. Display a menu:  

1. Add Book  

   2. Remove Book  

   3. View Book Collection  

   4. Get Total Books  

   5. Exit  

     
2. Depending on the user’s selection, call the appropriate class method to:  

   - Add a new book or update an existing one.  

   - Remove a specified quantity.  

   - Print a summary of all books.  

   - Show the total book count.  

"""

class Bookcollection:
    def __init__(self):
        self.books={}
        
    def add_book(self,title,book_quantity):
        if not title or book_quantity <=0:
            print("invalid title or book quantity....")
            return
        self.books[title] = self.books.get(title,0) + book_quantity
        print(f"add{book_quantity} copies of {title}.")
        
    def remove_book(self,title,book_quantity):
        if title not in self.book:
            print("book is not found...")
            
            return
        if book_quantity <=0 or book_quantity>self.books[title]:
            print("Invalid book quantity....")
            
            return
        self.books[title] = book_quantity
        
        if self.books[title] ==0:
            del self.books[title]
            print(f"remove all copies of {title}.")
            
    def view_books(self):
        if not self.books:
            print("No books in the collections..")
        
        return print("book collections:")
    
    for title,book_quantity in self.books.items():
        print(f"{title}:{book_quantity}copies")
        
        
    def get_total_books(self,total):
        self.total=total
        self.total =sum(self.books.values())
        print(f"Total number ofbooks: {self.total}") 
        
    def main():
        collection = Bookcollection()
        while True:
            print("\nBook Management System")
            print("1: add book")
            print("2: Remove book")
            print("3: View Total collection")
            print("4:Get total books")
            print("5:Exit")
            choice = input("choose an option...")
            
            if choice == "1":
                title =input("Enter book title:")
                book_quantity = input("Enter quantity:")
                
                if book_quantity.isdigit():
                    collection.add_book(title,int(book_quantity))
                
                else:
                    print("Invalid quantity. please enter positive no.")
            
            elif choice == "2":
                title = input("Enter the book title:")
                book_quantity = input("Enter the quantity to remove.")
                
                if book_quantity.isdigit():
                    collection.remove_book(title,int(book_quantity))
                else:
                    print("invalid quantity. please enter valid.")
                    
            elif choice == "3":
                collection.view_books()
            elif choice =="4":
                collection.get_total_books()
                
            elif choice =="5":
                print("Exiting program..")
                break
            else:
                print("Invalid choice. please select correct option.")
                
    
                    
        

        
    
    
            
        
        
        
        

