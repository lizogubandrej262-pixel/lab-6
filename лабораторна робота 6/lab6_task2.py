import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

def f(x):
    return math.exp(x) + math.sqrt(abs(x))

x = a
while x <= b + 1e-9:
    print(f"x = {x:.2f}   f(x) = {f(x):.4f}")
    x += h
