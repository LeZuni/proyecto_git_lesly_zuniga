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
    