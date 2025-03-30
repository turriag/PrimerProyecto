class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("samsung", "S23", "48MP")
celular2 = Celular("apple", "Iphone 15 pro", "50MP")


print(celular2.marca)