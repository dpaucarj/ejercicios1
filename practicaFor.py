class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre="Darwin"
        apellido="Paucar"
        numeros=(3,5,7,9,11)
        datos=["Patricio", 31, True]
        docente={'nombre':'Luis', 'edad':45, 'fac':'faci'}
        listaNotas=[(10,20),(80,50), (50,70)]
        listaAlumnos=[{"nombre":"Jairo", "final":90},{"nombre":"Andres", "final":71},{"nombres":"Diana", "final":99}]

        for i in range(10):
            print("i={}".format(i))
        for i in range(4,10,2):
            print("i={}".format(i), end=" ")    
        for i in range(12,3,-3):
            print("i={}".format(i), end="   ") 

        longitud=len(datos)  
        for i in range(longitud-1,0,-1):
            print("for", datos[i])
        for i, dato in enumerate(datos):
            print("for",i, dato)
        for dato in numeros:
            print(dato)

        print("\Diccionario de notas")
        for clave, valor in docente.items():
            print(clave, ":" ,valor, end="  ")
        for alumnos in listaAlumnos:
            for clave, valor in alumnos.items():
                print(clave, ":", valor, end="  ")        


bucle0=For()
bucle0.usoFor()