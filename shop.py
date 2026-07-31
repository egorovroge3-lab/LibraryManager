shop = [

    {
        "category":"Оружие",
        "items":[
            "Меч",
            "Лук",
            "Топор"
        ]
    },

    {
        "category":"Еда",
        "items":[
            "Яблоко",
            "Хлеб"
        ]
    }

]


карзина = []

print("=======================")
print("МАГАЗИН")
print("=======================")

def show_menu():
    print("Категории на выбор:")
    print("- Оружие")
    print("- Еда")
    print("1 - Карзина")

def save_items():

    save_it = input("В карзину: ").strip().capitalize()

    save = False

    for category in shop:

        for thing in category["items"]:

            if thing == save_it:

                print("В карзину добавлено:", thing)

                карзина.append(thing)

                save = True

    if not save:
        print("Такого товара нет")

def show_карзина():

        print("Ваша карзина:")

        print(карзина)

def search_shop():

    search = input("Поиск: ").strip().capitalize()

    if search == "1":

        show_карзина()

    else:

        found = False

        for category in shop:

            if category["category"] == search:

                print("Товары из категории", category["category"], ":")

                for items in category["items"]:

                    print("-", items)
        
                    found = True

                ask = input("Добавиь что нибудь в карзину? (да/нет): ").strip().capitalize()

                if ask == "Да":

                 save_items()

        if not found:
            print("Такой категории нет")
    


while True:

    show_menu()

    search_shop()
    
    back_menu = input("Вернуться в меню? (да/нет): ").strip().capitalize()

    if back_menu != "Да":
        break

