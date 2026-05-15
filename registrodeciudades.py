class Ciudad:
    def __init__(self, nombre, codigo_postal, poblacion, pais):
        self.nombre = nombre
        self.codigo_postal = codigo_postal
        self.poblacion = poblacion
        self.pais = pais

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codigo_postal": self.codigo_postal,
            "poblacion": self.poblacion,
            "pais": self.pais
        }
Zuñiga Lesli <leslymendez896@gmail.com>
	
2:39 p.m. (hace 45 minutos)
	
	
para mí
class Ciudad:
    def __init__(self, nombre, codigo_postal, poblacion, pais):
        self.nombre = nombre
        self.codigo_postal = codigo_postal
        self.poblacion = poblacion
        self.pais = pais

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codigo_postal": self.codigo_postal,
            "poblacion": self.poblacion,
            "pais": self.pais
        }

import json
import os

ARCHIVO = "ciudades.json"

def cargar_ciudades():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as file:
        return json.load(file)

def guardar_ciudades(ciudades):
    with open(ARCHIVO, "w", encoding="utf-8") as file:
        json.dump(ciudades, file, indent=4, ensure_ascii=False)

def mostrar_ciudades(ciudades):
    if not ciudades:
        print("\nNo hay ciudades registradas.")
        return

    print("\nLISTA DE CIUDADES")
    print("-" * 70)
    print(f"{'Nombre':15} {'CP':10} {'Población':15} {'País':15}")
    print("-" * 70)

    for ciudad in ciudades:
        print(
            f"{ciudad['nombre']:15} "
            f"{ciudad['codigo_postal']:10} "
            f"{ciudad['poblacion']:15} "
            f"{ciudad['pais']:15}"
        )

    print("-" * 70)