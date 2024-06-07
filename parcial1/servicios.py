import json

def imprimir_servicios(servicios):
    '''
    imprime una lista de servicios en formato de tabla
    '''
    encabezados = ["ID Servicio", "Descripción", "Tipo", "Precio Unitario", "Cantidad", "Total Servicio"]
    print(f"{encabezados[0]:<12} {encabezados[1]:<20} {encabezados[2]:<6} {encabezados[3]:<15} {encabezados[4]:<8} {encabezados[5]:<14}")
    print("="*75)
    for servicio in servicios:
        print(f"{servicio['id_servicio']:<12} {servicio['descripcion']:<20} {servicio['tipo']:<6} {servicio['precioUnitario']:<15} {servicio['cantidad']:<8} {servicio['totalServicio']:<14}")

def asignar_totales(servicios):
    '''
    asigna el totalServicio a cada servicio usando una funcion lambda.
    '''
    for servicio in servicios:
        servicio['totalServicio'] = float(servicio['precioUnitario']) * int (servicio['cantidad'])

def filtrar_por_tipo(servicios, tipo):
    """
    Filtra los servicios por tipo usando un bucle for.
    """
    servicios_filtrados = []
    for servicio in servicios:
        if servicio['tipo'] == tipo:
            servicios_filtrados.append(servicio)
    return servicios_filtrados

def ordenar_servicios(servicios):
    """
    Ordena los servicios por descripción en orden ascendente.
    """
    return sorted(servicios, key=lambda x:x['descripcion'])

def parse_json(archivo:str)-> list:
    with open(archivo, "r") as archivo:
        servicios = json.load(archivo)
    return servicios 

try:
    lista = parse_json("data.json")
    print(lista[0])
except FileNotFoundError:
    print("El archivo no existe")
except IndexError:
    print("Error de indice")