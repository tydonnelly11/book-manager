import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
   1: 'Show all books',
   2: 'Search by title',
   3: 'Search by ISBN',
   4: 'Search by publisher',
   5: 'Search in price range',
   6: 'Search by year',
   7: 'Search by title and publisher',
   8: 'return',
}

edit_book_options ={
    1: 'Change ISBN',
    2: 'Change title',
    3: 'Change year',
    4: 'Change publisher',
    5: 'Change previous edtion',
    6: 'Change price',
    7: 'Exit',
}

def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")


# def search_by_title():
#   To be added

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_submenu():
    print()
    print("Please make a selection")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()
def print_editbook():
    print("Select the imformation you would like to change")
    for key in edit_book_options.keys():
        print (str(key)+'.', edit_book_options[key], end = "  ")

def option1():
    pubName = str(input("Enter a publisher name (25 Character max)"))
    phone = str(input("Enter a 10 digit phone number with no -'s"))
    city = str(input("City name (20 character max)"))
    result = book_dao.insertPub(pubName,phone,city)
    print("done")
    print(result)


def option2():
    Isbn = str(input("Enter Isbn of book: "))
    title = str(input("Enter the title of book: ")) 
    year = int(input("Enter a year (4 character max): "))
    pub = str(input("Enter the publisher of the book: "))
    prevEd = str(input("Enter previous edition book if there is none hit enter: "))
    price = float(input("Enter the price of the book in the form xxxx.x: "))
    if prevEd == "":
        prevEd = None 
    result = book_dao.addBook(Isbn,title,year,pub,prevEd,price)
    print("done")
    
def option3():
    isbn = str(input("Enter ISBN of book you wish to edit"))
    if isbn not in book_dao.findAll():
        print("Book does not exist in database")
    else:
        while(True):
            print_editbook()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except KeyboardInterrupt:
                print('Interrupted')
                sys.exit(0)
            except:
                print('Wrong input. Please enter a number ...')

            if option == 1:
                newIsbn = str(input("Enter new ISBN"))
                book_dao.editISBN(isbn,newIsbn)
            elif option == 2:
                title = str(input("Enter new Title"))
                book_dao.editTitle(isbn,title)
            elif option == 3:
                year = str(input("Enter new year"))
                book_dao.editYear(isbn,year)
            elif option == 4:
                pub = str(input("Enter new publisher"))
                book_dao.editPub(isbn,pub)
            elif option == 5:
                prev = str(input("Enter new previous edition"))
                book_dao.editPrev(isbn,prev)
            elif option == 6:
                price = str(input("Enter new price"))
                book_dao.editPrice(isbn,price)
            elif option == 7:
                return
            

            

    


def option4():
    ISBN = str(input("Enter the ISBN of the book you wish to delete"))
    result = book_dao.deleteBook(ISBN)
    print("done")

def option5():
    while(True):
        print_submenu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')


        if option == 1:  #Finds all books
           results = book_dao.findAll()
           print("The following are the ISBNs and titles of all books.")
           for item in results:
                print(item[0], item[1])
           print("The end of books.")


        elif option == 2: #Finds books with specified title
            title = str(input('Enter title of book: '))
            results = book_dao.findByTitle(title)
            print("The following are the ISBNs and titles of books with the same title.")
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 3: # Finds books by ISBN
            Isbn = str(input('Enter ISBN of book: '))
            results = book_dao.findByISBN(Isbn)
            print("Book with ISBN "+ Isbn)
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 4: # Finds books by publisher
            pub = str(input('Enter publisher of books: '))
            results = book_dao.findByPub(pub)
            print("Books published by "+ pub)
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 5: # Finds book in price range
            min = str(input('Enter minimum price range: '))
            max = str(input('Enter max price range: '))
            results = book_dao.findByPrice(min,max)
            print("Books in price range of " + min + " to " + max + " dollars")
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 6: # finds book by year
            year = str(input('Enter year of books: '))
            results = book_dao.findByYear(year)
            print("Books published in "+ year)
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 7: # finds book by title and publisher
            title = str(input('Enter title of book: '))
            pub = str(input('Enter Publisher of book: '))
            results = book_dao.findByTitleAndPub(title,pub)
            print("The following are the ISBNs and titles of books with the same title and publisher")
            for item in results:
                print(item[0], item[1])
            print("The end of books.")
        elif option == 8: # returns to top menu
            return

        




if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option4 == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











