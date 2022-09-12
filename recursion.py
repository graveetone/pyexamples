'''
Рекурсія - це процес, коли функція викликає сама себе
'''


def function():  # оголошуємо функцію
    function()  # викликає саму себе


# function()  # викликаємо функцію один раз - далі вона викликатиме себе сама
'''
Рекурсію потрібно використовувати обережно, бо можна досягнути переповнення стеку
(Кожен виклик функції інтерпретатор поміщає в стек)
'''


def func3():
    pass


def func2():
    func3()


def func1():
    func2()


'''
Якщо викликати func1(), то стек матиме приблизно такий вигляд:

func3
func2
func1
'''
'''
Для рекурсії стек виглядає так:

func
func
func
func
...
func
func
...

Тобто, треба визначити, коли функція не буде знову викликати саму себе, щоб не було переповнення стеку
'''


def func(i):
    print(f'i = {i}')
    if i:
        func(i - 1)


func(5)
'''
Приклади використання рекурсії:
'''


def factorial(number):
    return 1 if number < 1 else number * factorial(number - 1)


print(factorial(5))  # 120


def fibonacci(number):
    return 1 if number < 2 else fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(5))  # 8
'''
Питання 1. Знайти довжину списка за допомогою рекурсії
'''


def recursive_len(list_):
    return recursive_len(list_[1:]) + 1 if list_ else 0


print(recursive_len([1, 2, 2, 3]))
'''
Питання 2. Знайти суму всіх елементів у вкладнеих списках за допомогою рекурсії
'''


def recursive_sum(list_):
    sum_ = 0
    for element in list_:
        if type(element) is list:
            sum_ += recursive_sum(element)
        else:
            sum_ += element
    return sum_


print(recursive_sum([1, [[2, 3], 4], 2, 4]))
