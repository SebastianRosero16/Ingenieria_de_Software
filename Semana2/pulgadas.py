def MetrosAPulgadas(metros):
    pulgadas = metros / 0.0254
    return pulgadas

metros = float(input('Ingrese la cantidad de tela en metros: '))
pulgadas = MetrosAPulgadas(metros)
print ('La cantidad de tela en pulgadas es: ', pulgadas)

