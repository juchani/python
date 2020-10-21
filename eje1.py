lst=[1, 2, [3,[4,5,6,[7,8],9],10],11,[12,13],14]
t=0
ot=0
def val(apla,st=0):
    global lista2
    lista=apla
    contador =0
    lista1=[]
    lista2=[]
    while contador==0:
        for l in lista:
            contador=2
            if isinstance(l,list):
                for r in l:
                    lista1.append(r)
                    
            else:
                lista1.append(l)
                #print(l)
    lista=lista1
    lista2.append(lista)
    
    for n in lista:
        if isinstance(n,list):
            #print("aun hay listas")
            val(lista)    
val(lst)
print(lista2[0])