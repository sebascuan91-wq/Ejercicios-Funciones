def maximodetres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor
x = int(input("A: "))
y = int(input("B: "))
z = int(input("C: "))
print("Mayor =", maximodetres(x, y, z))
