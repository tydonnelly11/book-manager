from mysql_connector import connection




def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
    

def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s;", (title,) 
    print(query)
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def findByISBN(ISBN):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN = %s;", (ISBN,) 
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def findByPub(Pub):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where published_by = %s;", (Pub,)
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def findByPrice(min,max):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price > %s and price < %s;", (min, max) 
    print(query)
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def findByYear(Year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year = %s;", (Year) 
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def findByTitleAndPub(title,pub):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title = %s and published_by = %s;", (title,pub) 
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close
    return results

def insertPub(name,phone,city):
    cursor = connection.cursor()
    query = 'insert into Publisher VALUES (%s,%s,%s)', (name,phone,city)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def deleteBook(isbn):
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where ISBN = %s;", (isbn,)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def addBook(isbn,title,year,pub,prevEd,price):
    cursor = connection.cursor()
    query = 'insert into Book VALUES (%s,%s,%s,%s,%s,%s)', (isbn,title,year,pub,prevEd,price)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editISBN(isbn,newIsbn):
    cursor = connection.cursor()
    query = 'update Book set ISBN = %s where ISBN = %s', (newIsbn, isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editTitle(isbn,title):
    cursor = connection.cursor()
    query = 'update Book set title = %s where ISBN = %s', (title, isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editYear(isbn,year):
    cursor = connection.cursor()
    query = 'update Book set year = %s where ISBN = %s', (year, isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editPub(isbn,pub):
    cursor = connection.cursor()
    query = 'update Book set published_by = %s where ISBN = %s', (pub, isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editPrev(isbn,prev):
    cursor = connection.cursor()
    query = 'update Book set previous_edition = %s where ISBN = %s', (prev, isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results

def editPrice(isbn,price):
    cursor = connection.cursor()
    query = 'update Book set price = %s where ISBN = %s', (price
    , isbn)
    print(query)
    cursor.execute(*query)
    results = cursor.fetchall()
    connection.close
    return results