import json

import text_tools

books = [
    { 
    "title": "1984",
    "author": "Джордж Оруэлл",
    "year": 1949,
    "available": True
     }
]

def load_file():

    try:

        file = open("book.json", "r")

        books = json.load(file)

        file.close()

        return books

    except FileNotFoundError:

        return []

def save_file():

    file = open("book.json", "w")

    json.dump(books, file, ensure_ascii=False, indent=4)

    file.close()

books = load_file()

def show_menu():
    print()
    print("ОНЛАЙН-БИБЛИОТЕКА")
    print()
    print("1 - Добавить книгу")
    print()
    print("2 - Показать все книги")
    print()
    print("3 - Найти книгу по названию")
    print()
    print("4 - Удалить книгу")
    print()
    print("0 - Выход")

# 1 добавить библиотеку
def add_book():

    title = input("Введите название книги: ")

    title = text_tools.normalize(title)

    found = False

    for book in books:

        if title == book["title"]:

            print("Такая книга уже есть")

            found = True

            break

    if not found:

        author = input("Введите имя фамилию автора: ")

        author = text_tools.normalize(author)

        try:

            year = int(input("Введите дату написания книги: ").strip())

            book = {
                "title": title,
                "author": author,
                "year": year,
                "available": True
                    }

            books.append(book)

            save_file()

            print("Книга успешно добавлена")

            print("Приятного чтения!")

        except:
    
            print("Введите дату используя толкьо цифры")


#2 показать библиотеку
def show_books():

    if not books:

        print("Пока тут пустовато")

    else:

        print("Ваши книги")
        print("===========")

        for book in books:

            print("Название:", book["title"])
            print("Автор:", book["author"])
            print("Год написания:", book["year"])

            if book["available"]:

                print("Статус: Доступна")

            else:

                print("Статус: Выдана")    

            print()

#3 найти книгу
def search_books():

    name = input("Введите название книги: ")

    name = text_tools.normalize(name)

    found = False

    for book in books:

        if name == book["title"]:

            print("Название:", book["title"])
            print("Автор:", book["author"])
            print("Год написания:", book["year"])

            if book["available"]:
            
                print("Статус: Доступна")
            
            else:
            
                print("Статус: Выдана")

            print("----------------------")

            found = True

            break

    if not found:

        print("Такой книги нет")  

#4 удалить книгу
def delete_book():

    if not books:

        print("Ваша библиотека пуста")

    else:

        for index, book in enumerate(books, start=1):

            print(index, book["title"])

        try:

            number_book = int(input("Ввыберите номер нужной книги: "))

            if number_book < 1 or number_book > len(books):

                print("Такой книги нет")

            else:

                books.pop(number_book - 1)

                print("Книга была удалена")

                save_file()

        except ValueError:

                print("Введите порядковый номер нужной вам книги")



while True:

    show_menu()

    try:

        action = int(input("Выберите действие: "))

        if action == 1:

            add_book()

        elif action == 2:

            show_books()

        elif action == 3:

            search_books()

        elif action == 4:

            delete_book()

        elif action == 0:

            print("До свидания!")
            break
    except ValueError:

        print("Введите только номер пункта")

    asc = input("Вернуться в меню? (да/нет): ")

    asc = text_tools.normalize(asc)

    if asc != "Да":

        print()

        print("До свидания!")

        break
                




         






