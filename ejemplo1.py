#creacion de la superclase "animal
class animal:
  #definir el metodo "sonido"
  def sonido(self):
    pass
#creacion de la subclase 1, junto con su metodo y atributo
class Perro(animal):
  #se asigna el mismo metodo de la superclase "animal"
  def sonido(self):
    return "Guau"
#creacion de la subclase 1, junto con su metodo y atributo
class Gato(animal):
  #se asigna el mismo metodo de la superclase "animal"
  def sonido(self):
    return "Miau"
#creacion de la funcion"hacer sonido"
hacer_sonido(animal:Animal):
  print(animal.sonido())

#creacion de los objetos
perro=Perro()
gato=Gato()

# salida de los objetos
hacer_sonido(perro)
hacer_sonido(gato)
