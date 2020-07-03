import time

# секундомер
# second = 0
# while True:
#  print(second)
#  time.sleep(1)
#  second += 1

# таймер (можно в секундах, в часах)
minutes = int(input("Сколько минут осталось? "))
seconds = minutes * 60
while True:
  # print(minutes)
  print(seconds)
  time.sleep(1) # задержка по секундам
  seconds -= 1
  if seconds == 0:
    print("Время вышло!")
    break