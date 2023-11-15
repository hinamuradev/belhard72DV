# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

while True:
    s = input()
    if s in ('+', '-', '*', '/'):
        a = float(input("a ="))
        b = float(input("b ="))

    match s:
        case '+':
            print(a+b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            if b != 0:
                print(a / b)
            else:
                print("Деление на нуль!")
        case 0:
            break
