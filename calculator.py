def meet():
    print("\nДобро пожаловать в калькулятор!")
    print("Доступные функции: +, -, *, /, **(возведение в степень), exit")
    calculator()


def meetSecond():
    print("\nЗачем приветствия? Ты уже знаешь где ты)!")
    print("Доступные функции: +, -, *, /, **(возведение в степень), exit")
    calculator()


def calculator():
    isFirstInpOkay = False
    func = input("Введи функцию из предложенных, которую хочешь использовать: ")

    if func == '+' or func == '-' or func == '*' or func == '/' or func == '**' or func == 'exit':
        print('Хорошо')
    else:
        print("Ошибка: неизвестная функция.")
        calculator()

    while True:

        if func == 'exit':
            print("Досвидания!")
            print("Для того, чтобы вернуться в калькулятор нажми любую клавишу.")
            input()
            meetSecond()

        try:
            if (isFirstInpOkay == False):
                num1 = float(input("Введи первое число: "))
                isFirstInpOkay = True
                num2 = float(input("Введи второе число: "))
            else:
                num2 = float(input("Введи второе число: "))
        except ValueError:
            print("Ошибка: пожалуйста, введи корректное число!")
            continue

        if func == '+':
            print(f"Результат: {num1 + num2}")
        elif func == '-':
            print(f"Результат: {num1 - num2}")
        elif func == '*':
            print(f"Результат: {num1 * num2}")
        elif func == '/':
            if num2 == 0:
                print("На ноль делить нельзя!")
            else:
                print(f"Результат: {num1 / num2}")
        elif func == '**':
            print(f"Результат: {num1 ** num2}")
        else:
            print("Ошибка: неизвестная функция.")
        print("Для того, чтобы вернуться в калькулятор нажми любую клавишу.")

        input()
        meetSecond()

meet()
