

tasks = []

def load_tasks():

    file_tasks = open("tasks.txt", "r")

    show_tasks = file_tasks.readlines()

    for show_task in show_tasks:
            
        tasks.append(show_task.strip())

    file_tasks.close()

def show_menu():
    print()
    print("================================="),
    print("Менеджер задач"),
    print("================================="),
    print(),
    print("1 - Добавить задачу"),
    print(),
    print("2 - Посмотреть задачи"),
    print(),
    print("3 - Удалить задачу"),
    print(),
    print("0 - Выход"),
    print(),


def save_tasks():

    file_tasks = open("tasks.txt", "w")

    for task in tasks:

        file_tasks.write(task + "\n")

    file_tasks.close()

load_tasks()

while True:
    show_menu()

    try:

        action = int(input("Выберите действие(1/2/3/0): "))

        if action == 1:

            tasks.append(input("Добавьте задачу: "))

            save_tasks()

        elif action == 2:

            if len(tasks) == 0:

                print("Задач пока нет.")
            else:

                for index, task in enumerate(tasks, start=1):

                    print(index, task)

        elif action == 3:

            if len(tasks) == 0:

                    print("Задач пока нет.")

            else:

                for index, task in enumerate(tasks, start=1):

                    print(index, task)
                
                try:

                    number_tasks = int(input("Ввыберите задачу: "))

                    if number_tasks < 1 or number_tasks > len(tasks):

                        print("Такой задачи нет")

                    else:
                
                        tasks.pop(number_tasks - 1)

                        print("Задача удалена")

                        save_tasks()

                except:

                    print("Введите порядковый номер записи")

            
        elif action == 0:

            print("До свидания!")
            break

    except:

        print("Введите только номер")


    menu = input("Вернуться в меню? (да/нет): ").strip().capitalize()   

    if menu != "Да":

        print("До свидания")
        break 