nombre="victor franco juchani"
voc=""
let=""
def bus(palabra):
    n1=0
    global voc
    global let
    lista=[]
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    for i in vocales:
        if i==palabra[0]:
            voc+=palabra[0]
            n1=1
        if palabra[0]==" ":
            n1=2
               
    if n1==0:
        let+=palabra[0]
    if n1==2:
        voc+=palabra[0]
        let+=palabra[0] 
        
    #print(palabra[0],n1,len(palabra))
    palabra=palabra[1:]
    if len(palabra)>0:
        bus(palabra)
    lista.append(let)
    lista.append(voc)
    
    print(lista)

bus(nombre)