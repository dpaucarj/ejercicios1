class Logica:
    def __init__(self, lista=None):
        self.__lista=lista 

    @property
    def lista (self):
        return self.__lista 
    @lista.setter
    def lista (self, value):
        self.__lista=value
        
    def parImpar(self, numero):
        rec=numero%2
        if rec==0:
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))   


    def perfecto(self, num):
        acu=0
        for contador in range (1,num):
            rec=num%contador
            if rec==0:
                acu=acu+contador 
        if acu==num:
            print("{} es perfecto".format(num))
        else:
            print("{} no es perfecto".format(num))        

class Ejercicio(Logica):
    def __init__(self, lista, numeros ):
        super().__init__(lista)
        self.dato=numeros

    def suma (self, n1, n2):
        return n1+n2

    def parImpar(self, numero):
        super().parImpar(numero)
        return numero%2  

ejer=Logica()
ejer.perfecto(8)

# ejer= Ejercicio([1,3,5],20)
# if ejer.parImpar(6)==0:
#     print("par")
# else:
#     print("impar")  

# print(ejer.lista)      

#print(ejer.suma(4,8))






#ejer=Logica([2,4,6])
#ejer.lista=[1,3]
#print(ejer.lista)
#num = int(input("ingrese numero:"))
#ejer.parImpar(num)
