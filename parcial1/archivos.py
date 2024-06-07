import json

def cargar_archivo(nombre_archivo):
    """
    Carga los datos desde un archivo JSON y devuelve una lista de servicios.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            servicios = json.load(archivo)
        return servicios
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

def guardar_archivo(nombre_archivo, datos):
    """
    Guarda los datos en un archivo JSON.
    """
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Datos guardados en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")