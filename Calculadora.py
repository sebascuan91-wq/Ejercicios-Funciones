def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b
def calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    op = int(input("Opción: "))
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    if op == 1:
        print(sumar(a, b))
    elif op == 2:
        print(restar(a, b))
    elif op == 3:
        print(multiplicar(a, b))
    elif op == 4:
        print(dividir(a, b))
calculadora()

