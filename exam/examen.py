class examen:                       #se crea la clase examen
    voc=""                          #se crean variables vacias de clase (atributo)
    let=""
    def bus(self,palabra):          #creamos un metodo (funcion en una clase)
        n1=0                        #creamos una variable igual a 0
        lista=[]                    #lista vacia
        vocales=["a","e","i","o","u","A","E","I","O","U"]#creamos una lista con las vocales que se quieren separar
        for i in vocales:           #creamos un bucle para separar las vocales 
            if i==palabra[0]:       #lo comparamos con el primer valor
                examen.voc+=palabra[0]#si son iguales se almacena en el atributo (variable) voc
                n1=1                #con esto descartamos tanto las consonates y los espacios
            if palabra[0]==" ":     #si hay espacios 
                n1=2                #n=2 
        if n1==0:                   #si no detecto nada es una consonante
            examen.let+=palabra[0]  #se asigna al atributo let  
        if n1==2:                   #si hay espacio 
            examen.voc+=palabra[0]  # se asigna a ambos atributos 
            examen.let+=palabra[0] 
        palabra=palabra[1:]         #se elimina la letra que uso
        if len(palabra)>0:          #se cuentan las letras para que no llegue a 0 y de error
            self.bus(palabra)       #si hay letras ejecutamos la misma funcion (recursividad)
        lista.append(examen.let)
        lista.append(examen.voc)    #se añade los valores a la lista 
        
        print(lista)                #se imprime
        
    def buscar(self):               # funcion para introducir texto (solo para el buscador)
        nombre=str(input("introduce el texto: ")) #introduce un texto
        self.bus(nombre)            #lo envia a la funcion anterior
        
        
    def identificar(self):          #funcion para identificar el tipo de variable
        valor=eval(input("introducir valor: ")) #la funcion eval convierte el valor que recibe al que se asemeja 
        if isinstance(valor,int):               #si valor es int 
            print(valor," es de tipo int")
    
        if isinstance(valor,float):             #si valor es float
            print(valor," es de tipo float")
            
        if isinstance(valor,str):               #si valor es str
            print(valor," es de tipo String")
        
        if isinstance(valor,list):              #si valor es lista
            print(valor," es una lista")
        
        if isinstance(valor,complex):           #si valor es complex
            print(valor," es de tipo complex")
        
        
    def multiplicar(self,v1,v2):                #creamos una funcion 
        v=0
        for i in range(v2):                     #basicamente sumamos las veces que nos indique
            v=v+v1

        print(v)                                #imprimimos 


