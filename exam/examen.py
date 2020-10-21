class examen:
    def buscar(self):
        nombre=str(input("introduce los nombres: "))
        n1=""
        n2=""
        l=0
        vocales=["a","e","i","o","u","A","E","I","O","U"," "] 
        for n in nombre:
            for c in vocales:
                if n==c:
                    n1+=n
                    l=1
                elif n==" ":
                    v=0
                else:
                    v=2
            print(n,v,l)
            if l==1:
                l=0
            elif l==0:
                n2+=n
            if v==0:
                n2+=" "
        lista=[n1,n2]
        print(lista)
        
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


