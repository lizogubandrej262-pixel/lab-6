import math

a = float(input("Введіть a : "))
b = float(input("Введіть b : "))
h = float(input("Введіть h : "))

spisok = []
x = a
while x <= b + 1e-9:
    y = math.exp(x) + math.sqrt(abs(x))
    spisok.append(y)
    x = x + h

print("список значень:")
print(spisok)

spisok.sort()

print("4 найменші елементи:")
print(spisok[:4])
