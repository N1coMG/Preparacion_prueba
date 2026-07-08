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
    for codigo_bodega in arreglos.keys():
        if codigo_bodega == codigo:
            return True
        else:
            return False

def actualizar_precio(busc_codigo, nuevo_precio, dicc_arreglos, bodega):
    verificacion = bsucar_codigo(busc_codigo, dicc_arreglos)
    if verificacion == True:
        for codigo, precio in bodega.items():
            if codigo == busc_codigo:
                precio[0] = nuevo_precio
                return True
    else:
        return False

def codigo_val(codigo_nv, arreglos):
    if len(codigo_nv) == 0:
        return False
    for codigo in arreglos.keys():
        if codigo == codigo_nv:
            return False
    return True

def nombre_val(nombre):
    if len(nombre) == 0:
        return False
    return True

def tipo_val(tipo):
    if len(tipo) == 0:
        return False
    return True

def color_val(color):
    if len(color) == 0:
        return False
    return True

def tamaño_val(tamño):
    if tamño != "S" and tamño != "M" and tamño != "L":
        return False
    return True

def tarjeta_val(tarjeta):
    if tarjeta == "s":
        return True
    elif tarjeta == "n":
        return False

def temporada_val(temporada):
    if len(temporada) == 0:
        return False
    return True

def precio_val(precio):
    try:
        precio_int = int(precio)
        if precio_int <= 0:
            return False
        return True
    except ValueError:
        return False

def unidades_val(unidades):
    try: 
        unidades_int = int(unidades)
        if unidades_int < 0:
            return False
        return True
    except ValueError:
        return False

def agregar_arreglo(codigo, nombre, tipo, color, tamaño, tarjeta, temporada, precio, unidades, dicc_arreglos, bodega):
            
    val_codigo = codigo_val(codigo, dicc_arreglos)
    val_nombre = nombre_val(nombre)
    val_tipo = tipo_val(tipo_nv)
    val_color = color_val(color)
    val_tamaño = tamaño_val(tamaño)
    val_tarjeta = tarjeta_val(tarjeta)
    val_temporada = temporada_val(tamaño)
    val_precio = precio_val(precio)
    val_unidad = unidades_val(unidades)
    
    if val_codigo == True and val_nombre == True and val_tipo == True and val_color == True and val_tamaño == True and val_temporada == True and val_precio == True and val_unidad == True:
        if tarjeta == "s":
            bool_tarj = True
        else:
            bool_tarj = False     
        dicc_arreglos[codigo] = [nombre, tipo, color, tamaño, bool_tarj, temporada]
        bodega[codigo] = [precio, unidades]
        return True
    for i in dicc_arreglos.keys():
        if i == codigo:
            print("El codigo ya existe")
    if val_codigo == False:
        print("ERROR: el campo de codigo es invalido")
    elif val_nombre == False:
        print("ERROR: El campo de nombre es invalido")
    elif val_tipo == False:
        print("ERROR: el campo de tipo es invalido")
    elif val_color == False:
        print("ERROR en campo de color")
    elif val_tamaño == False:
        print("ERROR en campo de tamaño")
    elif val_tarjeta == False:
        print("ERROR en campo de tarjeta")
    elif val_temporada == False:
        print("error en cmapo temporada")
    elif val_precio == False:
        print("ERROR en precio")
    elif val_unidad == False:
        print("ERROR en unidades")
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
            otro = "a"
            while otro != "n":
                busc_codigo = input("Ingrese codigo: ").upper().strip()
                while True:
                    try: 
                        nuevo_precio = int(input(f"Ingrese nuevo precio para {busc_codigo}: "))
                        if nuevo_precio > 0:
                            break
                        else:
                            print("El precio nuevo debe ser mayor a 0")
                    except ValueError:
                        print("Ingrese un valor numerico positivo.")
                existe = actualizar_precio(busc_codigo, nuevo_precio, dicc_arreglos, bodega)
                if existe == True:
                    print("Precio actualizado.")
                else:
                    print("El codigo no existe")
                while True:
                    otro = input("¿Desea actualizar otro precio (s/n)?").lower().strip()
                    if otro == "s" or otro == "n":
                        break
                    else:
                        print("Opcion invalida")
        case 4:
            print("")
            codigo_nv = input("Ingrese nuevo codigo: ").upper().strip()
            nombre_nv = input("Ingrese nuevio nombre: ").title().strip()
            tipo_nv = input("Ingrese nuevo tipo: ").lower().strip()
            color_pr_nv = input("Ingrese nuevo colo principal: ").lower().strip()
            tamaño_nv = input("Ingrese nuevo tamaño: ").upper().strip()
            inc_tarj_nv = input("Incluye tarjeta? (s o n) ").lower().strip()
            temporada_nv = input("Ingrese temporada: ").lower().strip()
            precio_nc = input("Ingrese precio: ").strip()
            unidades_nc = input("Ingrese unidades: ").strip()

            agregado = agregar_arreglo(codigo_nv, nombre_nv, tipo_nv, color_pr_nv, tamaño_nv, inc_tarj_nv, temporada_nv, precio_nc, unidades_nc, dicc_arreglos, bodega)
            if agregado == True:
                print("Arreglo Agregado")

        case 5:
            print("")
            #ya me voy a dormir, la logica de eliminar es simple, para eliminar la key con sus items,
            #solo debo usar del diccionario[key] y ya!!
        case 6:
            print("\nPrograma finalizado.")
        case _:
            print("\nDebe seleccionar una opción válida")