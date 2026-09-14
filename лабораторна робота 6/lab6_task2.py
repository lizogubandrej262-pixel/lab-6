import math

a = float(input("Введіть а : "))
b = float(input("Введіть b : "))
h = float(input("Введіть h : "))

x = a
while x <= b + 1e-9:
    y = math.exp(x) + math.sqrt(abs(x))
    print("x=%.1f y=%.3f" % (x, y))
    x = x + h
