lst=[1, 2, [3,[4,5,6,[7, [7,8],8],9],10],11,[12,13],14] #lista a aplanar 
                              ###### las variables de aqui estaban demas 
def val(apla,st=0):                  #creamos la funcion 
    global lista2                    #definimos una variable global para almacenar los datos definitivos 
    lista=apla                       #asignamos a lista los datos de entrada
    contador =0                      #contador es la variable para iniciar el bucle 
    lista1=[]                        #creamos listas vacias
    lista2=[]      
    while contador==0:
        for l in lista:              #inicia un bucle donde los datos de la lista se asignan a i
            contador=2               #en caso que no se ejecute ninguna condicion se sale del bucle
            if isinstance(l,list):   #si hay una lista inicia un for para aplanar 
                for r in l:          
                    lista1.append(r) #añade a lista1 los datos de la lista
            else:                    #
                lista1.append(l)     #si no hay lista añade los valores "sueltos"  
                #print(l)
    lista=lista1                     #asignamos a lista los valores de lista1 
    lista2.append(lista)             #añadimos los valores a la lista global
    
    for n in lista:                  #verificamos si hay listas dentro de lista
        if isinstance(n,list):       #si hay entonces...
            #print("aun hay listas")
            val(lista)               #ejecutamos la misma variable (recursividad)

val(lst)                             #ejecutamos la funcion funcion(lista)
print(lista2[0])                     #imprimimos el ultimo resultado de la lista global 