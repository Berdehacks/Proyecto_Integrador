print('7. Opcion propuesta: Conversor de tallas')


def usm_mxm(t):
    tmxm = (talla+18)
    return tmxm


def mxm_usm(t):
    tusm = (talla-18)
    return tusm


def usf_mxf(t):
    tmxf = (talla+17)
    return tmxf


def mxf_usf(t):
    tusf = (talla-17)
    return tusf


talla = float(input('Ingrese talla:'))
sexo = str(input('Ingrese sexo (M,F):'))
tipo_talla = str(input('Ingrese tipo de talla (MX, US):'))
tipo_a_conv = str(input('Ingrese a que tipo de talla convertir (MX, US):'))

if sexo == 'M' and tipo_talla == 'US' and tipo_a_conv == 'MX':
    conv = usm_mxm(talla)

if sexo == 'M' and tipo_talla == 'MX' and tipo_a_conv == 'US':
    conv = usm_mxm(talla)

if sexo == 'F' and tipo_talla == 'US' and tipo_a_conv == 'MX':
    conv = usm_mxm(talla)

if sexo == 'F' and tipo_talla == 'MX' and tipo_a_conv == 'US':
    conv = usm_mxm(talla)

if sexo == 'm' and tipo_talla == 'us' and tipo_a_conv == 'mx':
    conv = usm_mxm(talla)

if sexo == 'm' and tipo_talla == 'mx' and tipo_a_conv == 'us':
    conv = usm_mxm(talla)

if sexo == 'f' and tipo_talla == 'us' and tipo_a_conv == 'mx':
    conv = usm_mxm(talla)

if sexo == 'f' and tipo_talla == 'mx' and tipo_a_conv == 'us':
    conv = usm_mxm(talla)


print('Talla convertida: ', conv, ' MX')
