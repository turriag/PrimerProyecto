"""
Crea un programa que solicite el nombre, la edad y el pasatiempo favorito del estudiante. 
Después, verifica si el estudiante está realizando dicho pasatiempo en ese momento
"""
class Persona:
    def __init__(self, nombre, edad, pasatiempo_fav):
        self.nombre = nombre
        self.edad = edad
        self.pasatiempo_fav = pasatiempo_fav
    
    def disfrutar_pasatiempo(self):
        print(f"Disfrutando mi pasatiempo favorito: {self.pasatiempo_fav}")

nombre = input("Por favor, ingrese su nombre: ")
edad = input("Por favor, ingrese su edad: ")
pasatiempo = input("Por favor, ingrese su pasatiempo favorito: ")

persona = Persona(nombre, edad, pasatiempo)

print(f"""
        Datos de la persona: \n\n
        Nombre: {persona.nombre} \n
        Edad: {persona.edad} \n
        Pasatiempo favorito: {persona.pasatiempo_fav} \n
""")
while True:
    actividad = input("¿Cuál es tu hobby?: ")
    if actividad.lower() == persona.pasatiempo_fav.lower():
        persona.disfrutar_pasatiempo()
        break
    else:
        print("¡Inténtalo de nuevo!")




