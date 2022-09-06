''' 
Ітератор в Python - це об'єкт, що містить скінченну (зліченну) кількість елементів
За допомогою ітератора ми можемо отримувати значення поступово, по черзі
Теоретично, ітератором може бути будь-який об'єкт, що реалізує метод __next__() або метод __iter__()
Цикл for під капотом використовує ітератори. Під капотом це виглядає як створення ітератора і виклик методу __next__() на кожній ітерації 
'''

import random

class RandomStringIterator:
    CHARS = 'qwertyuiopasdfghjklzxcvbnm'
    def __init__(self):
        self.char = RandomStringIterator._get_random_char()
    def _get_random_char():
        return random.choice(RandomStringIterator.CHARS)

    def __iter__(self): 
        return self

    def __next__(self):
        random_char = self.char
        self.char = RandomStringIterator._get_random_char()
        return random_char
        
iterator = RandomStringIterator()

# print(RandomStringIterator().__get_random_char())

print('Let\'s test simple iterator:')
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for c in iter(random_string): # нескінченний цикл
    # print(c)
    
# print(len(list(iter(random_string)))) # тут ми не можемо отримати кількість елементів, бо ітератор ніколи не припиняє викликати метод next - це схоже на нескінченний цикл і по суті ми будемо мати нескінченну кількість випадкових символів
# Щоб обмежити кількість символів, яку ми ітератор буде повертати (по суті ми вказуємо скільки разів можна викликати метод next), використовують raise StopIteration
# Перепишемо ітератор так, аби можна було обмежити кількість випадкових символів

class RandomStringIteratorStoppable(RandomStringIterator):
    # CHARS = 'qwertyuiopasdfghjklzxcvbnm' # успадковується з предка
    
    def __init__(self, random_chars_count):
        super().__init__()
        self.random_chars_left = random_chars_count
        # self.char = RandomStringIteratorStoppable.__get_random_char() # замінимо на виклик init метода super
 
    # def __get_random_char():
    #     return random.choice(RandomStringIteratorStoppable.CHARS) # наслідуємо з базового класу

    # def __iter__(self): # наслідуємо з базового класу
    #     return self

    def __next__(self):
        if self.random_chars_left:
            random_char = self.char
            self.char = RandomStringIteratorStoppable._get_random_char()
            self.random_chars_left -= 1
            return random_char
        else:  # примітка! тут else можна пропустити, бо return вийде з функції і код після блоку if не виконається
            raise StopIteration 
            # коли ми отримаємо від ітератора потрібну кількість випадкових символів, то використаємо raise StopIteration statement. Це statement, а не Exception
            # коли ітератор зустріне цей стейтмент, то припинить викликати метод next і повертати випадкові символи
            # Спойлер: в масиві (list) також використовуються ітератори, завдяки чому ми можемо писати for element in [1, 2, 3 ]
            # Це означає, що клас Array в Python має методи iter та next. raise StopIteration для Array буде викликаний, коли ми дійдемо до останнього елементу - номер поточної ітерації буде рівний кількості елементів в масиві (len)
        
print('Let\'s test stoppable iterator:')
stoppable_iterator = RandomStringIteratorStoppable(3)

for char in stoppable_iterator:
    print(char)