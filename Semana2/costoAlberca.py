def CostoAlberca (largo, ancho, profundidad, costo_por_metro_cubico):
    volumen = largo * ancho * profundidad
    costo_total = volumen * costo_por_metro_cubico
    return costo_total

largo = float(input('Ingrese el largo de la alberca en metros: '))
ancho = float(input('Ingrese el ancho de la alberca en metros: '))
profundidad = float(input('Ingrese la profundidad de la alberca en metros: '))
costo_por_metro_cubico = float(input('Ingrese el costo por metro cubico de agua: '))

costo_total = CostoAlberca(largo, ancho, profundidad, costo_por_metro_cubico)
print(f'El costo total de la alberca es: {costo_total} pesos')