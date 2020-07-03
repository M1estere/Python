import time

def factorial(n):
  if n == 0:
    return 1

  f = 1
  i = 0

  while i < n: # пока число меньше заданного, будет умножаться
    i += 1
    f = f * i

  return f

def ser(a, b):
  c = input("Что нужно сделать?\n/ * + - % **\nFactorial(f) ")
  if c == "/":
    res = a / b
    print(res)
    return res

  elif c == "*":
    res = a * b
    print(res)

  elif c == "**":
    res = a ** b
    print(res)

  elif c == "+":
    res = a + b
    print(res)

  elif c == "-":
    res = a - b
    print(res)

  elif c == "%":
    res = a % b
    print(res)

  elif c.lower() == "f" or c.lower() == "factorial":
    number = int(input("Введите число для вычисления факториала: "))
    factorial(number)
    print("Факториал числа равен {f}".format(f = factorial(number)))

  else:
    print("Такой операции здесь нет")

while True:
  a, b = int(input("Введите первое число: ")), int(input("Введите   второе число: "))
  
  ser(a, b)
  