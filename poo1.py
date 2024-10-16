class Animal:
    def __init__(self,nombre,especie,edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def getNombre(self):
        return self.nombre
    def getEspecie(self):
        return self.especie
    def getEdad(self):
        return self.edad
    def mostrarAnimal(self):
        print("\nNombre:" +self.getNombre()+"\nEspecie: "+self.getEspecie()+"\nEdad: "+ str(self.getEdad())) 
    nombre = input("ingresar un animal:") 
    especie = input("diga que especie es:")
    edad = input("ingresar la edad del animal:")
    e = Animal(nombre,especie,edad)
    e.mostrarAnimal()    
    