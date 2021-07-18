class Operaciones:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        suma=self.numero1+self.numero2
        return suma

    def resta(self):
        # if self.numero1>=self.numero2:
        #    return self.numero1-self.numero2
        return self.numero1-self.numero2

    def multiplicacion(self):
        return self.numero1*self.numero2
        


    def division(self):
        if self.numero2!=0: return self.numero1//self.numero2
        return 0

    def divisionEntera(self):
        if self.numero2!=0: return self.numero1/self.numero2
        return 0
    
    def exponente(self):
        return self.numero1**self.numero2


    def mostar(self):
        print("operando1={}, operando2={}".format(self.numero1,self.numero2))
        
print("menu operaciones matematicas")
print("1) suma\n 2) resta\n 3) multiplicacio\n 4) division\n 5) division entera\n 6) residuo\n 7) exponente\n 8) salir" )
opc='0'
while opc !='8':
    opc= input("elija opcion [1...8]:")
    num1=int(input("ingrese numero1:"))
    num2=int(input("ingrese numero2:"))
    ope=Operaciones(num1,num2)

    if opc =='1': 
        print("{}+{}={}".format(ope.numero1,ope.numero2,ope.suma()))
    elif opc =='2':
        print("{}-{}={}".format(ope.numero1,ope.numero2,ope.resta()))
    elif opc=='3':
        print("{}*{}={}".format(ope.numero1,ope.numero2,ope.multiplicacion()))
print("gracias por su visita")        



# operacion=Operaciones(10,20)
# x=operacion.suma()
# #print(x) 
# y=operacion.resta()
# z=x**y
# print(z)
# operacion.mostar()

