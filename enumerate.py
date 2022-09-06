'''
Enumerate() - це функція, яка дозволяє при ітерації по обʼєкту отримати не лише обʼєкт, але і його індекс
https://www.programiz.com/python-programming/methods/built-in/enumerate
'''

array = [1, 2, 'Hello', True]

# Можна робити так:
print('Without enumerate')
index = 0
for element in array:
    print(f"Index: {index}")
    print(f"Element: {element}")
    index += 1

# Можна використати enumerate
print('With enumerate')
for index, element in enumerate(array, start=0):
    print(f"Index: {index}")
    print(f"Element: {element}")

# не обовʼязково використовувати for
print('Without for')
enumerated = enumerate(array)
print(f"Enumerate object: {enumerated}")
print(f"Converted to list: {list(enumerated)}")

# параметр start
print('Parameter start')
enumerated = enumerate(array, start=10)
print(f"Enumerate object: {enumerated}")
print(f"Converted to list: {list(enumerated)}")
