
continue_work = "да"

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "На ноль делить нельзя"
    
    return a / b

def get_numbers():
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))

    return number_one, number_two

def choose_action():
    action = input("Действие(+,-,*, /): ")

    return action



while continue_work == "да":
    
    number_one, number_two = get_numbers()

    action = choose_action() 
   
    if action == "+":
        print("Ответ:", add(number_one, number_two))
    elif action == "-":
        print("Ответ:", minus(number_one, number_two))
    elif action == "*":
        print("Ответ:", multiply(number_one, number_two))
    elif action == "/":
        print("Ответ:", divide(number_one, number_two))
    else:
        print("Неизвестная операция.")
    continue_work = input("Продолжить? (да/нет): ")

if continue_work == "нет":
    print("Конец")