
phones_book = {}

def insert_person(first, last, phone1=[]):
    pearson = (first, last)

    phones_book[pearson] = phone1

    return phones_book



def retrieving(first, last):
    
    return phones_book[(first, last)][0]

def delete(first, last):
    return phones_book.pop((first, last), None)

def print_n():
    for key, value in phones_book:
        print(key, value)

insert_person('Ala', 'Wiesołowska', ['+048 513 056 121', '22-848-34-21'])
print(phones_book)
print_n()