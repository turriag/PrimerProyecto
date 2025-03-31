"""
El programa debe solicitar al usuario el nombre, la edad y su asignatura favorita. 
Luego, debe verificar si el estudiante está realizando alguna actividad relacionada con estudiar
"""

class Estudiante:
    def __init__(self, nombre, edad, asignatura_favorita):
        self.nombre = nombre
        self.edad = edad
        self.asignatura_favorita = asignatura_favorita
    
    def estudiar(self):
        print("Estudiando...")
nombre = input("por favor, digite su nombre: ")
edad = input("por favor, digire su edad: ")
asignatura_favorita = input("por favor, ingrese su asignatura favorita: ")

Estudiante = Estudiante(nombre, edad, asignatura_favorita)

print(f"""
        Datos del estudiante: \n\n
        nombre: {Estudiante.nombre} \n
        edad: {Estudiante.edad} \n
        asignatura_favorita: {Estudiante.asignatura_favorita} \n

""")
while True:
    estudiando = input("En estos momentos que hace?: ")
    if (estudiando.lower() == "estudiando"):
        Estudiante.estudiar()
        break  
    else:
        print("Intentalo de nuevo")


