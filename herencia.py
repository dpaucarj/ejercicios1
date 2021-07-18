class Persona:
    _siguiente=0
    def __init__(self, nombre="invitado", activo=True):
        Persona._siguiente=Persona._siguiente+1
        self.__codigo= Persona._siguiente+1
        self.__nombre=nombre
        self.activo=activo
@property
def nombre (self):
    return self.__nombre
@nombre.setter
def nombre(self,nom):
    self.__nombre=nom
@property
def codigo(self):
    return self.__codigo
@codigo.setter
def codigo(self, cod):
    self.__codigo=cod           
per1=Persona()
print(per1.codigo)        