from random import randint
import time

while True:
  a = input("Хотите поиграть? Да/Нет: ")

  if a.lower() =="да":
    b, c = randint(1, 6), randint(1,6)

    print(f"Боту выпало: {b}")
    time.sleep(0.5)

    print(f"Вам выпало: {c}")
    time.sleep(1)

    if b > c:
      print("Вы проиграли :(")

    elif c > b:
      print("Вы выиграли :)")

    else:
      print("ВАУ!\nНичья")

  elif a.lower() == "нет":
    print("Прощайте\nСкоро увидимся!")
    break
    
  else:
    print("Не понятно")