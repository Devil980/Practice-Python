import os
class library:
    def __init__(self):
        self.book_file = "Library_book.txt"
        self.no_of_books = 0
        self.book = []

        if os.path.exists(self.book_file):
            with open(self.book_file, "r") as file:
                self.books = [line.strip() for line in file]
            self.no_of_books = len(self.books)
    def add_book(self,book):
        if book in self.book:
            print(f"{book} is already in the library")
            return
        self.book.append(book)
        self.no_of_books += 1
        # print(f"{book} has been added to the library")
        with open(self.book_file, "a") as file:
            file.write(book + "\n")
            # print(f"{book} has been added to the library")
    def print_book(self):
        for i, book in enumerate(self.book,start=1):
            print(f"{i}. {book}") 
    def get_no_of_book(self):
        return self.no_of_books
    def is_book_present(self,book):
        return book in self.book
    
my_library = library()

my_library.add_book("Harry Potter")
my_library.add_book("Pride and Prejudice")
my_library.add_book("48 laws of power")
my_library.add_book("The Great Gatsby")
my_library.add_book("To kill a mocking bird")
my_library.add_book("1984")
my_library.add_book("The Book Theif")
my_library.add_book("Animal Farm")
my_library.add_book("It ends with us")


# print("My Library: ")
# my_library.print_book()

# print(f"Numbers of Book: {my_library.get_no_of_book()}")
add = input("Do You want to add book or print the book in the library? type (y) for yes or (n)for no: ")
if add.lower() == "yes" or add.lower() == "y":
    get_books = input("Enter the Name of the book you want to add: ")
    if my_library.is_book_present(get_books):
        print(f"{get_books} is already in the library")
    else:
       my_library.add_book(get_books)
# elif add == "print":
#     print("My Library: ")
#     my_library.print_book()
#     print(f"Numbers of Book: {my_library.get_no_of_book()}")
else:
    print("Its great please continue")


print("My Library: ")
my_library.print_book()
print(f"Numbers of Book: {my_library.get_no_of_book()}")

Search = input("Do you want to search book? Type (y) yes or (n) for no: ")
if Search.lower() == "yes" or Search.lower() == "y":
  get_books = input("The Name of the book: ")
  if my_library.is_book_present(get_books):
    print(f"{get_books} is available in ")
  else:
    print(f"Sorry {get_books} is unavailable")
elif Search.lower() == "no" or Search.lower() == "n":
    print("Thanks, Have a great day")