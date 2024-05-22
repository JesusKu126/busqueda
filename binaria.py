def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return False

mi_lista_ordenada = [1, 3, 4, 5, 6, 9, 11, 15, 18, 21]
elemento_a_buscar = 6

if busqueda_binaria(mi_lista_ordenada, elemento_a_buscar):
    print(f"El elemento {elemento_a_buscar} está en la lista.")
else:
    print(f"El elemento {elemento_a_buscar} no está en la lista.")
