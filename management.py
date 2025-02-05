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
    def init(self):
        self.book = {}

    def add_book(self, title, quantity):
        if title in self.book:
            self.book[title] += quantity
        else:
            self.book[title] = quantity

    def remove_book(self, title, quantity):
        if title in self.book:
            if self.book[title] >= quantity:
                self.book[title] -= quantity
                if self.book[title] == 0:
                    del self.book[title]
            else:
                print("Not enough books to remove")
        else:
            print("Book not found")

    def view_book(self):
        for title, quantity in self.book.items():
            print(f"{title} : {quantity}")

    def total_book(self):
        return sum(self.book.values())

def main():
    collection = Bookcollection()
    while True:
        choice = input("\n1. Add 2. Remove 3. View 4. Total 5. Exit: ")
        if choice == '1':
            collection.add_book(input("Title: "), int(input("Quantity: ")))
        elif choice == '2':
            collection.remove_book(input("Title: "), int(input("Quantity: ")))
        elif choice == '3':
            collection.view_book()
        elif choice == '4':
            print(f"Total books: {collection.total_book()}")
        else:
            break

main()
    
                    
        

        
    
    
            
        
        
        
        

