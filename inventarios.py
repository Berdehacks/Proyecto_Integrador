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
# print(Ventas)


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


# registrar_venta()
# registrar_ingreso()
# consultar_inventario()
# consultar_articulo()
