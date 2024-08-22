def EncontrarMayorValor (num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else: 
        return "Los números son iguales"

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = EncontrarMayorValor(num1, num2)
print (resultado)

