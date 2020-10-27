class operacion:                               #se crea la clase
    def identificar(self):                     #se crea el metodo
        msg=input("introduzca la operacion ")  #Se crea una entrada
        try:                                   #se ejecutara esta parte si no hay error
            n=msg.find("*")                    #buscara el simbolo de multiplicacion 
            if n>0:                            #si se encuentra el simbolo 
                a=msg[:n]                      #se conbierte en float los valores antes del * y despues 
                b=msg[n+1:]                    
                a=float(a)
                b=float(b)
                print(a*b)                     #se imprime la ooperacion
            ############################ es lo mismo solo que con distintos simbolos  
            n=msg.find("+")
            if n>0:
                a=msg[:n]
                b=msg[n+1:]
                a=float(a)
                b=float(b)
                print(a+b)
            n=msg.find("-")
            if n>0:
                a=msg[:n]
                b=msg[n+1:]
                a=float(a)
                b=float(b)
                print(a-b)
            n=msg.find("/")
            if n>0:
                a=msg[:n]
                b=msg[n+1:]
                a=float(a)
                b=float(b)
                print(a/b)
        #################################### Las excepciones se ejecutan en caso que ocurra un error en la seccion try       
        except(ValueError):                       #especificamos el value error se da en caso de float("A") 
            print("Solo numeros son permitidos")
        except(ZeroDivisionError):                #este error es en caso que se divida por cero
            print("No es posible division entre 0")
        
