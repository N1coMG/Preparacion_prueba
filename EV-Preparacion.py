dicc_arreglos = {
 'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
 'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
 'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
 'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
 'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
 'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
 'FLO1': [15990, 8],
 'FLO2': [29990, 3],
 'FLO3': [9990, 12],
 'FLO4': [24990, 5],
 'FLO5': [19990, 0],
 'FLO6': [22990, 6],
}

opcion = 0

def leer_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================
""")
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-6)"))
            return opcion
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_tipo(arreglos, bodega, tipo):
    cant_arreglos = 0
    encontrado = False
    for codigo, arreglo in arreglos.items():
        if tipo == arreglo[1]:
            for codigo_bodega, cant in bodega.items():
                if codigo == codigo_bodega:
                    cant_arreglos += cant[1]
                    encontrado = True
    if encontrado == True:
        print(f"\nEl total de unidades disponibles para {tipo}: {cant_arreglos}")
    else:
        print(f"\nEl tipo {tipo}, no esta registrado.")

def busqueda_precio(bodega, p_minimo, p_maximo, arreglos):
    lista_arreglos = []
    for codigo, cant_arreglo in bodega.items():
        precio = cant_arreglo[0]
        if precio >= p_minimo and precio <= p_maximo and cant_arreglo[1] > 0:
            for codigo_arreglo, nombre in arreglos.items():
                if codigo == codigo_arreglo:
                    lista_arreglos.append(f"{nombre[0]}--{codigo_arreglo}")
    if len(lista_arreglos) > 0:
        lista_arreglos.sort()
        for i in lista_arreglos:
            print(i)
    else:
        print("No hay arreglos en ese rango de precios.")

def bsucar_codigo(codigo, arreglos):
    for codigo_bodega in arreglos.key():
        if codigo_bodega == codigo:
            return True
        else:
            return False


while opcion != 6:
    opcion = leer_menu()
    match opcion:
        case 1:
            print("\n>>>Unidades por tipo de arreglo")
            tipo_arreglo = input("\nIngrese un tipo de arreglo:\n").lower().strip()
            unidades_tipo(dicc_arreglos, bodega, tipo_arreglo)
        case 2:
            print(">>> Busqueda de arreglos por rango de precio")

            try:
                p_minimo = int(input("Ingrese el precio minimo: "))
                p_maximo = int(input("Ingrese el precio maximo: "))
                if p_minimo >= 0 and p_maximo >= 0 and p_maximo > p_minimo:
                    busqueda_precio(bodega, p_minimo, p_maximo , dicc_arreglos)
                else:
                    print("ERROR: Ingrese valores validos.")
            except ValueError:
                print("ERROR: Ingrese valores enteros.")
        case 3:
            print("")
            busc_codigo = input("Ingrese codigo: ").upper().strip()
            existe = bsucar_codigo(busc_codigo, dicc_arreglos)
        case 4:
            print("")
        case 5:
            print("")
        case 6:
            print("\nPrograma finalizado.")
        case _:
            print("\nDebe seleccionar una opción válida")