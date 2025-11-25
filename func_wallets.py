import json
import os

archivousers = "usuarios_wallets.json"

def cargar_wallets():
    if os.path.exists(archivousers): # si existe el archivo "archivousers" en la ruta
        with open(archivousers, "r") as f: #se abre en modo lectura y se lo asigna a f
            return json.load(f)#lee f y lo convierte desde json a python en dict o list
    return {} #si el archivo no existe devolvemos un diccionario vacio

def guardar_wallets(data):
    with open(archivousers, "w") as f: #abre o crea el archivousers en escritura y se asigna a f
        json.dump(data, f, indent=4)#guarda data (o sino un dict o cualquier otro obj) en un archivo transformandolo a json, le pasamos el archivo a donde guardar, y el indent es el nivel de sangria, en este caso 4 espacios

def agregar_wallet(user_id, wallet):
    data = cargar_wallets()

    if str(user_id) not in data: #user_id es un numero, entonces lo hacemos str
        data[str(user_id)] = [] #si el usuario no existe en el archivo lo creamos y le asignamos una lista vacia
    
    if wallet not in data[str(user_id)]:
        data[str(user_id)].append(wallet)
        guardar_wallets(data)
        return True
    return False   
def borrar_wallet(user_id, wallet):
    data = cargar_wallets()

    if str(user_id) not in data:
        return "No existen wallets registradas."
    
    if wallet not in data[str(user_id)]:
        return "La wallet no se encuentra registrada."
    
    data[str(user_id)].remove(wallet)

    guardar_wallets(data)

    return f"La wallet {wallet} fue eliminada correctamente."    


