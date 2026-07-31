def show_menu():
    print()
    print("ПРОФИЛЬ ИГРОКА")
    print()
    print("1 - показать профиль")
    print()
    print("2 - изменить уровень")
    print()
    print("3 - изменить количество монет")
    print()
    print("4 - Изменить имя игрока")
    print()
    print("5 - Показать всех игроков")
    print()
    print("6 - Поиск игроков")
    print()
    print("0 - выхож")
    print()

def load_players():

    file_players = open("players.txt", "r")
# s значит save сохранить кароч
    s_players = file_players.readlines()

    for s_player in s_players:

        players.append(s_player.strip())

    file_players.close()


def save_players():

    file_players = open("players.txt", "w")

    for player in players:

        file_players.write(player + "\n")

    file_players.close()

current_player ={

        "name": "Chort17",
        "health": 122,
        "coins": 500,
        "level": 67
    }

players = [
    {
        "name": "Егор",
        "level": 15,
        "coins": 500
    },
    {
        "name": "Иван",
        "level": 7,
        "coins": 300
    }
]

def choose_action():
    action = int(input("Выберите действие(1,2,3,4,5,6,7,0): "))

    return action
def show_profile():
    print("Имя игрока:", current_player["name"])
    print("Здоровье:", current_player["health"])
    print("Монеты:",current_player["coins"])
    print("Уровень:",current_player["level"])

def change_lvl():
    print("Ваш уровень:",current_player["level"])
    current_player["level"] = int(input("Изминение уровня: "))


def change_coins():
    print("Ваши монеты:",current_player["coins"])
    current_player["coins"] = int(input("Изминение количества монет: "))

def change_name():
    print("Имя игрока:", current_player["name"])
    current_player["name"] = input("Изменить имя игрока: ")
    print("Ваше имя успешно изменино, теперь вы:", current_player["name"])

def show_players():
    for index, player in enumerate(players, start=1):
           print("Игрок №", index)
           print("Имя:", player["name"])
           print("Монеты:", player["coins"])
           print("Уровень:", player["level"])
           print("----------------------")

def search_players():
    name = input("Введите имя: ")
    
    name = name.capitalize()

    found = False

    for player in players:

        if player["name"] == name:

            print("Имя игрока:", player["name"])
            print("Уровень игрока:", player["level"])
            print("Монеты:", player["coins"])

            found = True

            break

    if not found:
        print("Игрок не найден")   


def add_players():

    name = input("Введите имя игрока: ").strip().capitalize()

    lvl = int(input("Введите уровень игрока: "))

    coins = int(input("Введите кол-во монет игрока: "))

    players.add(name)
    players.add(lvl)
    players.add(coins)


def new_players():

    add_players = input("Добавить игрока? (да/нет): ").strip().capitalize()

    if add_players == "Да":

        add_players()


def exit_menu():
    print("конец")

while True:

    show_menu()

    action = choose_action()

    if action == 1:
        show_profile()
    elif action == 2:
        change_lvl()
    elif action == 3:
        change_coins()
    elif action == 4:
        change_name()
    elif action == 5:
        show_players()
    elif action == 6:
        search_players()
    elif action == 7:
        add_players()
    elif action == 0:
        exit_menu()
        break
    else:
        print("Такого пункта нет")

    ask = input("Вернуться в меню? (да/нет): ").strip().capitalize()

    if ask == "Нет":
        break