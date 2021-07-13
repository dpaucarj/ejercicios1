class cargoOcupacion:
    secuencia =0
    def __init__(self, des="sin cargo"):
        cargoOcupacion.secuencia=cargoOcupacion.secuencia+1  
        self.codigo=cargoOcupacion.secuencia 
        self.descripcion=des


carg1=cargoOcupacion()
#cargo1.codigo=1
#cargo1.descripcion="docente"
print(carg1.codigo, carg1.descripcion )
carg2=cargoOcupacion()
carg2.descripcion="director" 
print(carg2.codigo, carg2 .descripcion) 
carg3= cargoOcupacion("analista")
print(carg3.codigo, carg3.descripcion)        