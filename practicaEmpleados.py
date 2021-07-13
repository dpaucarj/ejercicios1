from practicaCargo import cargoOcupacion
class trabajador:
    secuencia=0
    def __init__(self, nom, ced, sue, cargos):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargos

    def mostrar (self):
        print("codigo:{} nombre:{} cargo:{}-{}". format(self.codigo, self.nombre, self.cargo.codigo, self.cargo.descripcion))    


    def generarCodigo(self):
        trabajador.secuencia=trabajador.secuencia+1
        return trabajador.secuencia

cargo1=cargoOcupacion("docente")
emp1=cargoOcupacion("darwin", "0845", 5655, cargo1 )
emp1.mostrar()        








if __name__=="_main_":