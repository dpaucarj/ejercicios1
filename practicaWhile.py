class cicloWhile:

    def __init__(self, car1=0):
        self.caracter=car1


    def usoWhile(self):
        dato=input("ingrese dias: ")
        dato=dato.lower()
        while dato not in ("lunes", ",martes", "miercoles", "jueves", "viernes", "sabado", "domingo"):
            dato=input("ingrese dias: ").lower()
        print("***FELICITACIONES*** {} es un dia ".format(dato))


caracter=cicloWhile()
caracter.usoWhile()            




    