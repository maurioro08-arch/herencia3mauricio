from clases.herencia1.taxi import Taxi 
from clases.herencia1.auto_particular import AutoParticular

def main(): 
    coche = Taxi("123-GTO","Versa",1000,"123-a") 
    print(coche) 
    coche.encender() 
    coche.subirPasajeros() 
    coche.acelerar() 
    coche.frenar() 
    coche.cobrarCuota() 
    ap = AutoParticular("123","Mauricio",18,"volvo","plata","987-G")
    print(ap)
    ap.subirseAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajandoAuto()
if __name__ == '__main__': 
    main()