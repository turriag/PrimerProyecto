class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")

nombre = input("por favor, digite su nombre: ")
edad = input("por favor, digite su edad: ")
grado = input("por favor, digite su grado: ")

Estudiante = Estudiante(nombre, edad, grado)

print(f"""
        Datos del estudiante:\n\n
        Nombre: {Estudiante.nombre} \n
        Edad: {Estudiante.edad} \n
        Grado: {Estudiante.grado} \n

""")
while True:
    estudiando = input("En estos momentos que haces?: ")
    if (estudiando.lower() == "estudiando"):
        Estudiante.estudiar()
        break
    else:
        print("intentalo de nuevo")