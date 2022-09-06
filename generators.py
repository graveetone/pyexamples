# The yield statement suspends a function’s execution 
# and sends a value back to the caller, but retains 
# enough state to enable the function to resume where 
# it left off. When the function resumes, it continues 
# execution immediately after the last yield run. 
# This allows its code to produce a series of values over time, 
# rather than computing them at once and sending them back like a list.

# Ключове слово return надсилає якесь значення в точку виклику
def divider():
    print('-' * 30)
def return_some_value():
    return 123

returned_value = return_some_value() # тут знаходиться точка виклику - умовно кажучи - той рядок коду, де ми викликаємо функцію чи метод
print(returned_value)
divider()
# функція return_some_value повертає сюди (в точку виклику) число 123, тому цей рядок виглядає так returned_value = 123

# Ключове слово return також виходить з функції - ПРИПИНЯЄ її виконання
def return_some_value2():
    print('I will be printed because return IS NOT ABOVE me')
    return 123 # це значення поверне функція
    print("I will never be printed because return IS ABOVE me")
returned_value2 = return_some_value2()
print(returned_value2)
divider()
# Ключове слово yield також надсилає якесь значення в точку виклику (як і return)
def yield_some_value()
    yield 123

yielded_value = next(yield_some_value()) # так в пайтон 3
# yielded_value = yield_some_value().next() # так було в пайтон 2
print(yielded_value)
divider()
# Ключове слово yield також ставить функцію на паузу - ПРИЗУПИНЯЄ її виконання

def yield_some_value2()
    print('I will be printed')
    yield 123 # функція поверне це значення і поставить функцію на паузу 
    print(I will be printed too because we use yield)
    yield 'TEST STRING' # ми можемо повернути ще щось при виклику цієї функції

generator = yield_some_value2()
first_yielded_value = next(generator)
print(first_yielded_value) # очікуємо тут 123
divider()

second_yielded_value = next(generator)
print(second_yielded_value) # очікуємо тут 'TEST STRING'
divider()

# third_yielded_value = next(generator) # очікуємо тут 
# print(third_yielded_value)
divider()

# httpswww.geeksforgeeks.orguse-yield-keyword-instead-return-keyword-python

# в контексті генераторів часто згадують також 'list comprehension' - 'спискові включення', 'включення списків' тощо
# LC - це зручний спосіб створювати масиви (або словники - це dictionary comprehension) на основі, наприклад, інших масивів
list_comp = [x  2 for x in range(10) if x % 2 == 0] # list_comp - масив, в якому збережені парні квадрати чисел 0..10 
gen_exp = (x  2 for x in range(10) if x % 2 == 0)   # gen_exp - це вираз генератора (правило за яким буде генеруватися кожен елемент)
                                                      # правило те саме - парні квадрати чисел 0..10
print('Example of LC ', list_comp)
print('Example of generator', gen_exp)
print('First way to get generated elements')
print(next(gen_exp)) # 1 gen value
print(next(gen_exp)) # 2 gen value
print(next(gen_exp)) # 3
print(next(gen_exp)) # 4
print(next(gen_exp)) # 5
# АБО
print('Second way to get generated elements (more popular and convenient)')
gen_exp = (x  2 for x in range(10) if x % 2 == 0)  # створюємо генератор знову, інакше не отримаємо нічого
for i in list(gen_exp)                              # бо в генератора не буде чисел, які підходять під правило
    print(i)                                         #  (парні квадрати чисел 0..10)

from sys import getsizeof
print('LC size', getsizeof(list_comp))
print('Generator size', getsizeof(gen_exp))
# легше запам'ятати правило і застосувати його - легше запам'ятати, що 314^2 = 314  314 = 98596
# ніж запам'ятати результат                    - ніж одразу запам'ятати, що 314^2 = 98596