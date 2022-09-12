print('-CODE1-')
CONST = 4
print(CONST)
CONST = 43
print(CONST)

print('-CODE2-')
змінна = 3
print(змінна)

print('-CODE3-')
x = 5
y = 3
c = complex(x,y);
  
# printing real and imaginary part of complex number
print ("The real part of complex number is : ",end="")
print (c.real)
  
print ("The imaginary part of complex number is : ",end="")
print (c.imag)

print(f'Complex number: {c}')

print('-CODE4-')
print(f'Abs of 3: {abs(3)}')
print(f'Abs of -3: {abs(-3)}')
print(f'Round of 3.342: {round(3.342)}')

import math
print(f'trunc of 3.342: {math.trunc(3.342)}')

print(f'floor of 3.342: {math.floor(3.342)}')
print(f'ceil of 3.342: {math.ceil(3.342)}')
print(f'pi: {math.pi}')
print(f'e: {math.e}')
print(f'sin of 3.342: {math.sin(3.342)}')
print(f'cos of 3.342: {math.cos(3.342)}')

print('-CODE5-')

x, y = True, True
print(f'{x} and {y} equals {x and y}')
print(f'{x} or {y} equals {x or y}')

x, y = True, False
print(f'{x} and {y} equals {x and y}')
print(f'{x} or {y} equals {x or y}')

x, y = False, True
print(f'{x} and {y} equals {x and y}')
print(f'{x} or {y} equals {x or y}')

x, y = False, False
print(f'{x} and {y} equals {x and y}')
print(f'{x} or {y} equals {x or y}')

x = True
print(f'not {x} equals {not x}')

x = False
print(f'not {x} equals {not x}')

print('-CODE6-')
x = None # can be explicitly False or 0 or ''
y = x or 1
p = x and 1
print(f'or = {y}')
print(f'and = {p}')

x = 3
y = x or 1
p = x and 1
print(f'or = {y}')
print(f'and = {p}')

print('-CODE7-')

x = ["apple", "banana", "cherry"]

y = ["apple", "banana", "cherry"]

print(f"Equality with '=' : {x == y}")
print(f"Equality with 'is' : {x is y}")

print('-CODE8-')

x = 4

print(x > 0 and x < 10)
print(0 < x < 10)
print(x in range(-1, 10))

print('-CODE9-')
arr = [1, 2, 3]
print(arr)
print(arr, sep=' SEPARATOR ')
print(arr, end=' END OF LINE ')
print(arr, file=open('tst.txt', 'w'))
print(arr, flush=True)

print('-CODE10-')

x = -10
print(f'x = {x}')
var = x if x > 0 else 1
print(f'var = x if x > 0 else 1 ===>  {var}')
var = x if x < 0 else 2
print(f'var = x if x < 0 else 2 ===>  {var}')

print('-CODE11-')

string = 'hello'
print('not empty' if string else 'empty')

string = ''
print('not empty' if string else 'empty')

number = -11
print('not zero' if number else 'zero')

number = 0
print('not zero' if number else 'zero')

arr = [1, 2]
print('not empty' if arr else 'empty')

arr = []
print('not empty' if arr else 'empty')

print('-CODE12-')

i = 0
while i < 3:
  print(i)
  i += 1

i = 0
while i < 3:
  print(i)
  i += 1
else:
  print('end of while')

for i in range(2):
  print(i)

for i in range(2):
  print(i)
else:
  print('end of for')

for i in range(6):
  if i == 4:
    break
    
  if i == 1:
    continue

  print(i)

i = 0
while True:
  if i == 2:
    break
  print('hi')
  i += 1

print('-CODE13-')

def f():
  print(1)

x = f() # NONE BECAUSE NO RETURN

print(x)

def fun(x):
  if not x:
    return
  else:
    print(x)

fun(0)

fun(4)

print('-CODE14-')

def fun(x, y, c='default'):
  print(x, y, c)

fun(1, 2)
fun(y=1, x=2)

fun(1,2, c='custom')
fun(y=1,x=2, c='custom')

print('-CODE15-')
def function():
  '''
  I AM USEFUL DESCRIPTION
  '''
  pass

print('-CODE16-')

def a():
  def b():
    pass
  pass

a()
# b() # error

print('-CODE17-')

x = 1 # global

def f():
  v = 4 # local
  global x # specify that we use global x
  x = 3  

f()
print(x)
# print(v) # error

print('-CODE18-')

arr = [1, 2, 3]
print(arr[0])
print(arr[-1])
print(arr[-3])

s = 'hello world'
print(s[0])
print(s[-1])
print(s[-3])

print(s[3:8:2]) # l o