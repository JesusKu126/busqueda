def busqueda_secuencial(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
elemento_a_buscar = 6

if busqueda_secuencial(mi_lista, elemento_a_buscar):
    print(f"El elemento {elemento_a_buscar} está en la lista.")
else:
    print(f"El elemento {elemento_a_buscar} no está en la lista.")
