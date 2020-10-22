#

# seccion de inventario
matriz = []
archivo = open('inventarios.csv', 'r')
for linea in archivo:
    matriz.append(linea.split(','))
archivo.close()
# print(matriz)

inventario = {}
for i in matriz:
    # print(i[0])
    inventario[i[0]] = {
        'marca': i[1],
        'talla': i[2],
        'color': i[3],
        'cantidad': int(i[4]),
        # 'vendidos': i[5]
    }
    # inventario[i[0]]['vendidos'] = (
    #     inventario[i[0]]['vendidos'].replace('\n', ''))

# print(inventario)

matrizVendedores = []
archivoVendedores = open('vendedores.csv', 'r')
for linea in archivoVendedores:
    matrizVendedores.append(linea.split(','))
archivoVendedores.close()
vendedores = {}
for i in matrizVendedores:
    # print(i[0])
    vendedores[i[0]] = {
        'nombre': i[1],
        'apellido': i[2]
    }
    vendedores[i[0]]['apellido'] = (
        vendedores[i[0]]['apellido'].replace('\n', ''))

# seccion ventas

matrizVentas = []
archivoVentas = open('ventas.csv', 'r')
for linea in archivoVentas:
    matrizVentas.append(linea.split(','))
archivoVentas.close()
# print(matrizVentas)

Ventas = {}
for i in matrizVentas:
    # print(i[0])
    Ventas[i[0]] = {
        'Air Force 1': int(i[1]),
        'Yeezy': int(i[2]),
        'Ultra Range': int(i[3]),
        'Air Max': int(i[4]),
        'Ralph Sampson': int(i[5]),
        'Ultra Boost': int(i[6]),
        'Skyve Max': int(i[7])}
    # Ventas[i[0]]['vendidos'] = (
    # inventario[i[0]]['VSkyve'].replace('\n', ''))
print(Ventas)


# seccion vendedores
listaVendedores = []
for vendedor in matrizVendedores:
    listaVendedores.append(vendedor[0])
# print(listaVendedores)

listaModelos = []
for modelo in inventario:
    listaModelos.append(modelo)
# print(listaModelos)


ventasTotales = {}
for i in listaModelos:
    ventasTotales = {
        'Air Force 1': ((Ventas['jp001']['Air Force 1'])+(Ventas['am002']['Air Force 1'])+(Ventas['ac003']['Air Force 1'])+(Ventas['er004']['Air Force 1'])+(Ventas['mh005']['Air Force 1'])),
        'Yeezy': ((Ventas['jp001']['Yeezy'])+(Ventas['am002']['Yeezy'])+(Ventas['ac003']['Yeezy'])+(Ventas['er004']['Yeezy'])+(Ventas['mh005']['Yeezy'])),
        'Ultra Range': ((Ventas['jp001']['Ultra Range'])+(Ventas['am002']['Ultra Range'])+(Ventas['ac003']['Ultra Range'])+(Ventas['er004']['Ultra Range'])+(Ventas['mh005']['Ultra Range'])),
        'Air Max': ((Ventas['jp001']['Air Max'])+(Ventas['am002']['Air Max'])+(Ventas['ac003']['Air Max'])+(Ventas['er004']['Air Max'])+(Ventas['mh005']['Air Max'])),
        'Ralph Sampson': ((Ventas['jp001']['Ralph Sampson'])+(Ventas['am002']['Ralph Sampson'])+(Ventas['ac003']['Ralph Sampson'])+(Ventas['er004']['Ralph Sampson'])+(Ventas['mh005']['Ralph Sampson'])),
        'Ultra Boost': ((Ventas['jp001']['Ultra Boost'])+(Ventas['am002']['Ultra Boost'])+(Ventas['ac003']['Ultra Boost'])+(Ventas['er004']['Ultra Boost'])+(Ventas['mh005']['Ultra Boost'])),
        'Skyve Max': ((Ventas['jp001']['Skyve Max'])+(Ventas['am002']['Skyve Max'])+(Ventas['ac003']['Skyve Max'])+(Ventas['er004']['Skyve Max'])+(Ventas['mh005']['Skyve Max']))}

# print(ventasTotales)
ventasVendedor = {}
for i in listaVendedores:
    ventasVendedor[i] = ((Ventas[i]['Air Force 1'])+(Ventas[i]['Yeezy'])+(Ventas[i]['Ultra Range'])+(
        Ventas[i]['Air Max'])+(Ventas[i]['Ralph Sampson'])+Ventas[i]['Ultra Boost'] + Ventas[i]['Skyve Max'])
# print(ventasVendedor)


def registrar_venta():
    # print(cantidadAlmacen)
    while True:
        matricula = input('Ingrese matricula del vendedor: ')
        modelo = input('Ingrese modelo: ')
        cantidad = int(input('Ingrese Cantidad: '))
        if (modelo in listaModelos):
            cantidadAlmacen = inventario[modelo]['cantidad']
            if (matricula in listaVendedores) and (cantidad <= cantidadAlmacen):  # ADD verificacion modelo
                inventario[modelo]['cantidad'] = (
                    inventario[modelo]['cantidad']) - cantidad
                print('Venta completada')
                print('Cantidad nueva', inventario[modelo]['cantidad'])
                # agregar ventas a diccionario de ventas
                Ventas[matricula][modelo] = (
                    Ventas[matricula][modelo]) + cantidad
                break
            else:
                print('Verifica tu informacion')
        else:
            print('modelo invalido')


def registrar_ingreso():
    modelo = input('Ingrese modelo: ')
    cantidad = int(input('Ingrese Cantidad: '))
    while True:
        if (modelo in listaModelos):
            # ADD verificacion modelo
            inventario[modelo]['cantidad'] = (
                inventario[modelo]['cantidad']) + cantidad
            print('Agregado correctamente')
            print('Cantidad nueva', inventario[modelo]['cantidad'])
            break
        else:
            print('modelo invalido')


def consultar_inventario():
    modelo = input('Ingrese modelo: ')
    if modelo in listaModelos:
        print('pares restantes', inventario[modelo]['cantidad'])
    else:
        print('modelo invalido')


def consultar_articulo():
    max_value = max(ventasTotales.values())  # maximum value
    # getting all keys containing the `maximum`
    max_keys = [k for k, v in ventasTotales.items() if v == max_value]
    print('los articulos con mas ventas son: ', max_keys,
          ' con ', max_value, ' articulos vendidos')


def consultar_vendedor():
    max_value = max(ventasVendedor.values())  # maximum value
    # getting all keys containing the `maximum`
    max_keys = [k for k, v in ventasVendedor.items() if v == max_value]
    print('El vendedor con mas ventas es: ', vendedores[max_keys[0]]['nombre'], vendedores[max_keys[0]]['apellido'],
          ' con ', max_value, ' articulos vendidos')


def reporte_ventas():
    matricula = str(input('Ingrese matricula del vendedor: '))
    while True:
        if (matricula in listaVendedores):
            nombre_reporte = (f'{matricula}_reporteVentas.txt')
            print(nombre_reporte)
            nombre = vendedores[matricula]['nombre']
            apellido = vendedores[matricula]['apellido']

            AirForce = Ventas[matricula]['Air Force 1']
            Yeezy = Ventas[matricula]['Yeezy']
            UltraRangeExo = Ventas[matricula]['Ultra Range']
            AirMax = Ventas[matricula]['Air Max']
            RalphSampson = Ventas[matricula]['Ralph Sampson']
            UltraBoost = Ventas[matricula]['Ultra Boost']
            SkyveMax = Ventas[matricula]['Skyve Max']

            reporte = open(nombre_reporte, 'w')
            # texto = f'{vendedores[matricula]['nombre']}{ vendedores[matricula]['apellido']} \n {ventasVendedor[matricula]}'
            texto = (
                f'{nombre} {apellido}' + '\n' +
                f'Air Force 1: {AirForce}'+'\n' +
                f'Yeezy: {Yeezy}'+'\n' +
                f'Ultra Range: {UltraRangeExo}'+'\n' +
                f'Air Max 97: {AirMax}'+'\n' +
                f'Ralph Sampson: {RalphSampson}'+'\n' +
                f'Ultra Boost: {UltraBoost}'+'\n' +
                f'Skyve: {SkyveMax}')
            print('Archivo generado correctamente')
            reporte.write(texto)
            reporte.close()
            break
    else:
        print('Matricula incorrecta ')


def guardar_ventas():
    for vendedor in Ventas:
        texto = (
            f'{Ventas[[0]]},'
        )


def volver_a_menu():
    while True:
        retu = input('<Presione X para regresar>')
        if retu == 'X':
            break
    menu()


def menu():
    while True:
        print('''
    Menú principal
    1. Registrar una venta
    2. Registrar llegada de artículos al almacén
    3. Consultar el inventario disponible
    4. Consultar cuál es el modelo del artículo más vendido
    5. Consultar cuál vendedor ha vendido una cantidad mayor de artículos
    6. Reporte de ventas de un vendedor
    7. conversor de tallas 
    8. Salir del programa''')
        while True:
            opcion = int(input('Seleccione su opción:'))
            if opcion == 1:
                registrar_venta()
                volver_a_menu()
            elif opcion == 2:
                registrar_ingreso()
                volver_a_menu()
            elif opcion == 3:
                consultar_inventario()
                volver_a_menu()
            elif opcion == 4:
                consultar_articulo()
                volver_a_menu()
            elif opcion == 5:
                consultar_vendedor()
                volver_a_menu()
            elif opcion == 6:
                reporte_ventas()
                volver_a_menu()
            elif opcion == 7:
                import conversor
                volver_a_menu()
            elif opcion == 8:
                break


# menu()

# registrar_venta()
# registrar_ingreso()
# consultar_inventario()
# consultar_articulo()
# consultar_vendedor()
# print(vendedores)
# reporte_ventas()
