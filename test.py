def iterate()
  arr = []
  for i in range(10):
    if i % 2 == 0:
      arr.append(i * i)
  return arr
end

a = iterate()

print(a)

a = [i**2 for i in range(10) if i % 2 == 0]
print(a)
