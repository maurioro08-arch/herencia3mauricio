from clases.herencia2.persona import Persona

class AutoParticular(Persona):
    def __init__(self, clave, nombre, edad, marca, color, placa):
        super().__init__(clave, nombre, edad)
        self.marca = marca
        self.color = color
        self.placa = placa
    #metodo str
    def __str__(self):
        return super().__str__()+" "+self.marca+" "+self.color+" "+self.placa+" "
    
    #Metodo funcionales
    def subirseAuto(self):
        print("subiendo al auto")
    def arrancarAuto(self):
        print("Encendiendo el raio")
        print("Arrancando el motor")
    def llegarDestino(self):
        print("Llegando al destino")
    def bajandoAuto(self):
        print("Bajando del auto")