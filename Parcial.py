from UTN_Heroes_Dataset.utn_pp import (
    get_original_matrix, mostrar_matriz_texto_tabla)

# Punto 1
matriz_concesionaria = get_original_matrix()
#print(matriz_concesionaria)

def cargar_datos(matriz):
    """ Reordena la matriz en una nueva.

    Args:
        (matriz): La matriz que va a ser ordenada.

    Returns:
        devuelve la matriz ordenada.
    """
    nueva_matriz = []

    for j in range(len(matriz[0])):
        fila = [j + 1, matriz[0][j], matriz[1][j], matriz[2][j], matriz[3][j], matriz[4][j]]
        nueva_matriz.append(fila)
    
    return nueva_matriz

nueva_matriz = cargar_datos(matriz_concesionaria)
lista_nombre_colunas = [ "Garaje N", "marca", "modelo", "unidades", "precio", "ganancia" ]
mostrar_matriz_texto_tabla(nueva_matriz, lista_nombre_colunas)

# Punto 2
def obtener_autos_totales(matriz):
    """ Suma los autos totales en todos los garages.

    Args:
        (matriz): La matriz que contiene la informacion.

    Returns:
        devuelve la suma de todos los autos.
    """
    cantidad_autos_totales = 0
    for fila in matriz:
        cantidad_autos_totales += fila[3]

    return cantidad_autos_totales

autos_totales = obtener_autos_totales(nueva_matriz)
print(f"La cantidad de autos totales es: {autos_totales}")

# Punto 3
def obtener_garage_con_menos_autos(matriz):
    """ Busca cual es el garage con menos unidades.

    Args:
        (matriz): La matriz que contiene la informacion.

    Returns:
        devuelve el numero de garage q menos autos tiene.
    """
    garage_con_menos_unidades = 0
    menor_unidades = 100
    for fila in nueva_matriz:
        garage_id = fila[0]
        unidades = fila[3]

        if unidades < menor_unidades:
            menor_unidades = unidades
            garage_con_menos_unidades = garage_id
    
    return garage_con_menos_unidades

garage_menos_unidades = obtener_garage_con_menos_autos(nueva_matriz)
print(f"El garage con menos vehiculos es el numero {garage_menos_unidades}")

#Punto 4
def obtener_garage_con_mas_autos_y_cantidad(matriz):
    """ Busca cual es el garage con mas unidades y cuantas son.

    Args:
        (matriz): La matriz que contiene la informacion.

    Returns:
        devuelve el numero de garage q mas autos tiene y la cantidad.
    """
    meyor_unidad = 0
    garage_con_mas_unidades = 0

    for fila in matriz:
        garage_id = fila[0]
        unidades = fila[3]

        if unidades > meyor_unidad:
            meyor_unidad = unidades
            garage_con_mas_unidades = garage_id
    
    lista = [garage_con_mas_unidades, meyor_unidad]
    return lista


garage_menos_unidades = obtener_garage_con_mas_autos_y_cantidad(nueva_matriz)
print(f"El garage con mas unidades es el {garage_menos_unidades[0]} y tiene {garage_menos_unidades[1]} unidades")

#Punto 5
def obtener_recaudacion(matriz):
    """ Calcula la recaudacion total.

    Args:
        (matriz): La matriz que contiene la informacion.

    Returns:
        devuelve la recaudacion total.
    """
    recaudacion_total = 0

    for fila in matriz:
        unidades = fila[3]
        precio = fila[4]
        recaudacion_total += unidades * precio
    
    return recaudacion_total

recaudacion_total = obtener_recaudacion(nueva_matriz)
print(f"La recaudacion total de todos los garages es: ${recaudacion_total}")

#Punto 6
def cantidad_de_garages_con_seis_o_mas_unidades(matriz):
    """ Calcula la cantidad de garages que albergan 6 o mas unidades.

    Args:
        (matriz): La matriz que contiene la informacion.

    Returns:
        devuelve la cantidad de garajes que tienen 6 o mas unidades.
    """
    cantidad_garages = 0

    for fila in matriz:
        unidades = fila[3]

        if unidades >= 6:
            cantidad_garages += 1

    return cantidad_garages
    
cantidad_garages = cantidad_de_garages_con_seis_o_mas_unidades(nueva_matriz)
print(f"La cantidad de garages con mas de 6 unidades es: {cantidad_garages}")