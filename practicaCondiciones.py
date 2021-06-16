class condicion:
    inicio=0

    def __init__(self, dat1=0, dat2=6):
        self.dato1=dat1
        self.dato2=dat2
        self.dato3=dat2

    def usoIf(self):
        if self.dato1==self.dato2:
            print("dato1: {}, dato2: {}: son iguales". format(self.dato1, self.dato2))
        elif self.dato1==self.dato3:
            print ("dato1: {}, dato3: {}: son iguales". format(self.dato1, self.dato3))
        else:
            print("no son iguales")


presentacion=condicion()
presentacion.usoIf()
print(presentacion.dato2)            


