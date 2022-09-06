'''
У Python можна використовувати _ (underscore) для різних задач
'''

#1 в інтерпретаторі
import os
# os.system("python3") # виконуємо команду python3 в терміналі
# _ можна використовувати, як змінну, що містить попереднє значення
#2 ігнорування значень
array = [1, 2, 3, 4, 5]
one, *_, five = array # пропускаємо усі значення, крім першого та останнього
print(one, five)

#3 як змінна в циклі (не рекомендовано - лише, якщо змінна - просто лічильник)

array = [1, 2, 3, 4, 5]
for _ in array:
  print(_) # нерекомендовано

for _ in range(3):
  print('Hello') # допустимо

#4 візуальне розділення великих чисел

big_number = 10000000000000
readable_big_number = 10_000_000_000_000 # інтерпретатор проігнорує _ в цьому
print(big_number == readable_big_number) # випадку, але це читабельно

#5 _variable
from helpers import * # імпортуємо усе
# print(_test_function()) # тут помилка

# можливий інший варіант
class Test:
  def __init__(self):
    self._protected_variable = 123

print(Test()._protected_variable) # не робить змінну protected насправді

#6 variable_
# class = 1  # невалідна змінна
class_ = 1   # валідна змінна

#7 __variable - name mangling
class Test:
  def __init__(self):
    self.__private_variable = 1234

# print(Test().__private_variable) # захищена змінна - недоступна
print(Test()._Test__private_variable) # але до неї можна доступитися

#8 __name__
# https://www.tutorialsteacher.com/python/magic-methods-in-python#:~:text=Python%20%2D%20Magic%20or%20Dunder%20Methods,class%20on%20a%20certain%20action.

class Test:
  def __init__(self, value):
    self.value = value

  def __add__(self, other):
    return self.value + other.value

print(Test(1) + Test(3))
print(Test(1).__add__(Test(3)))
    
