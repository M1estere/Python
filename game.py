while True:
  k = input("Хочешь сыграть в игру? Да/Нет ")
  if k.lower() == "да":

    # Настройки
    a = 1
    b = 100
    print(f'Загадай число от {a} до {b}...')

    # Определим свою функцию, которая напечатает правила
    def print_rules():
        rules = '''Если я угадаю, напиши "=",\nесли твое число меньше -     пиши"<",\nа если больше - пиши">".\nИ нажми на Enter.'''
        print()  # Пустая строка
        print(rules)
        print()

    # время
    import time
    time.sleep(2)
    print('Загадал?')
    time.sleep(1)
    print('Тогда начинаем!')
    time.sleep(1)
    print_rules()
    time.sleep(1)

    # Отгадываем
    steps = 0

    while True:
        if a > b:
            print('Ошибка')
            break
        elif a == b:
            print(f'Легко. Ответ - {a}')
            print(f'Потребовалось шагов: {steps}')
            break

        steps += 1

        number = (a + b) // 2
        answer = input(f'Это {number}? ')

        if answer == '=':
            print('Я молодец, что снова отгадал!')
            print(f'Потребовалось шагов: {steps}')
            break

        elif answer == '<':
            b = number - 1

        elif answer == '>':
            a = number + 1

        else:
            print('Не понял. На всякий случай напомню правила:')
            print_rules()
            steps -= 1

    print('Спасибо за игру!')
  elif k.lower() == "нет":
    print("В другой раз :(")
    break
  else:
    print("Я не понимаю\nПопробуем снова")
