def invertir(cad):
    if cad == "":
        return ""
    return invertir(cad[1:]) + cad[0]
def espalindromo(cad):
    if cad == invertir(cad):
        return True
    else:
        return False
pal = input("Cadena: ")
print(espalindromo(pal))
