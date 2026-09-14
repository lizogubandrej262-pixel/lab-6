import math

a=float(input("введіть а: "))
b=float(input("введіть b: "))
h=float(input("введіть h: "))

x = a
n = int((b - a) / h) + 1

for i in range(n):
    y = math.exp(x) + math.sqrt(abs(x))
    print("%i x=%.1f y=%.3f" % (i,x,y))
    x = x + h
