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
        'VAirForce1': int(i[1]),
        'VYeezy': int(i[2]),
        'VUltraR': int(i[3]),
        'VMax': int(i[4]),
        'VRalph': int(i[5]),
        'VUltraB': int(i[6]),
        'VSkyve': int(i[7])}
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
for i, j in zip(listaModelos, listaVendedores):
    ventasTotales[i] = 0 + Ventas[i][j]
print(ventasTotales)


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


# registrar_venta()
# registrar_ingreso()
# consultar_inventario()
