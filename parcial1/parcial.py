import json
from archivos import *
from servicios import *
from biblioteca import *


servicios = []
servicios = parse_json("data.json")

while True:
    mostrar_menu()   
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
        servicios = cargar_archivo(nombre_archivo)
    elif opcion == '2':
        if servicios:
            imprimir_servicios(servicios)
        else:
            print("No hay servicios cargados.")
    elif opcion == '3':
        if servicios:
            asignar_totales(servicios)
            print("Totales asignados correctamente.")
        else:
            print("No hay servicios cargados.")
    elif opcion == '4':
        tipo = input("Ingrese el tipo de servicio a filtrar (1-MINORISTA, 2-MAYORISTA, 3-EXPORTAR): ")
        servicios_filtrados = filtrar_por_tipo(servicios, tipo)
        if servicios_filtrados:
            guardar_archivo(f"servicios_tipo_{tipo}.json", servicios_filtrados)
        else:
            print("opcion no valida, intente nuevamente.")
    elif opcion == '5':
        if servicios:
            servicios_ordenados = ordenar_servicios(servicios)
            imprimir_servicios(servicios_ordenados)
        else:
            print("No hay servicios cargados.")
    elif opcion == '6':
        if servicios:
            servicios_ordenados = ordenar_servicios(servicios)
            nombre_archivo = input("Ingrese el nombre del archivo a guardar: ")
            guardar_archivo(nombre_archivo, servicios_ordenados)
        else:
            print("No hay servicios cargados")
    elif opcion == '7':
        print("Saliendo.")
        break
    else: 
        print("Opcion no valida. Intente nuevamente.")

