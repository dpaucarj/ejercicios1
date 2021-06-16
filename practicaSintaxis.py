class Sintaxis:
    inicio =0

    def __init__(self, nota="comienzo"):
        self.oracion= nota

    def usoVariables(self):

        edad, peso=31, 70
        nombre="Darwin"
        tipoSexo="M"
        casado=True
        print (nombre, edad)

        usuario=()
        usuario=("dpaucarj", 321, "dpaucarj@gmail.com", True )
        materias=[]
        materias=["circuitos", "sistemasOperativos", "redes"]
        docente={}
        docente={"nombre":"Darwin", "edad":31, "fac":"faci"}
        print("""mi nombre es {}, tengo {}, anos""".format(nombre, edad))    


prac1=Sintaxis()
prac1.usoVariables()    
        

