lista=[5,2,6,4,7,8,9]
for i in lista:
    print(i)
    pass
x=2
for pos in range(x+1,len(lista)):
    print(pos, lista[pos])    

for pos, ele in enumerate(lista):
    print(pos, ele )        
    pass