class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    
    def llamar(self):
        print(f"Estas haciendo una llamada desde un: {self.modelo}")

    def cortar(self):
        print(f"Cortar la llamada desde un: {self.modelo}")


celular1 = Celular("samsung", "S23", "48MP")
celular2 = Celular("apple", "Iphone 15 pro", "50MP")

celular1.llamar()
