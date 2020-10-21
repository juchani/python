class examen:
    voc=""
    let=""
    def bus(self,palabra):
        n1=0
        lista=[]
        vocales=["a","e","i","o","u","A","E","I","O","U"]
        for i in vocales:
            if i==palabra[0]:
                examen.voc+=palabra[0]
                n1=1
            if palabra[0]==" ":
                n1=2         
        if n1==0:
            examen.let+=palabra[0]
        if n1==2:
            examen.voc+=palabra[0]
            examen.let+=palabra[0] 
        palabra=palabra[1:]
        if len(palabra)>0:
            self.bus(palabra)
        lista.append(examen.let)
        lista.append(examen.voc)
        
        print(lista)
        
    def buscar(self):
        nombre=str(input("introduce el texto: "))
        self.bus(nombre)
        
    def identificar(self):
        valor=eval(input("introducir valor: "))
        if isinstance(valor,int):
            print(valor," es de tipo int")
    
        if isinstance(valor,float):
            print(valor," es de tipo float")
            
        if isinstance(valor,str):
            print(valor," es de tipo String")
        
        if isinstance(valor,list):
            print(valor," es una lista")
        
        if isinstance(valor,complex):
            print(valor," es de tipo complex")
        
        
    def multiplicar(self,v1,v2):
        v=0
        est=0
        if v1<0:
            est=est+1
            v1=v1*-1
        if v2<0:
            est=est+1
            v2=v2*-1
        for i in range(v2):
            v=v+v1
            
        if (est+est)==1:
            v=v*-1
            
        print(v)


