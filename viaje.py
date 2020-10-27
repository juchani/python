################# creamos una lista con todas las rutas
dt=[["SCZ" , "cotoca" , 7],
["SCZ" , "porongo" , 2],
["SCZ" , "pailon" , 3],
["SCZ" , "samaipata" , 4],
["cotoca" , "porongo", 3],
["cotoca" ,"buena vista" ,4],
["porongo" , "buena vista" , 4],
["porongo" , "minero" , 5],
["pailon" , "okinawa" , 2],
["buena vista" , "montero", 1],
["montero" , "minero" , 3],
["warnes" , "minero", 2],
["warnes" , "CBBA" ,2],
["carrasco" , "san julian" , 6],
["carrasco" , "vallegrande" , 4],
["carrasco" , "okinawa" , 4],
["san julian", "minero" , 1],
["vallegrande", "CBBA", 5]]



origen="SCZ"                                      # origen 
destino="CBBA"                                    # destino 


a=[]
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]
m=[m1,m2,m3,m4,m5]
e=[]
valor_f=[]

estado=0
s=0
c=0
c1=0
v1=0
v2=0
v3=0
v4=0
v5=0
total=[]

for i in dt:                                      #creamos un bucle for 
    if i.count(origen)>0 and i.index(origen)==0:  #se buscan las listas que inicien con el origen 
        a.append(i)                               # si es asi se añaden a la lista a


for i in a:                                       #creamos un for para leer la lista a 
    for r in dt:                                  #creamos un for para leer la lista dt
        if r[0]==i[1]:                            #si coinciden el primer valor de r y el segundo valor de i
            if r[0]==destino:                     #si hay coincidencias entre r[0] y destino 
                print(c,"destino encontrado",i)   
                estado=1                          #se setea estado a 1 para evitar que se repita el valor
                valor_f.append(c)                 #se almacena el conteo en valor_f
                m[c].append(i)                    #se añade a la lista anidada m
                s=1                               #s=1 para ajustar la notificacion al final
            elif r[1]==destino:                   #si hay coincidencias entre r[1] y destino
                m[c].append(r)                    #se añade a m para determinar la ruta 
                m[c].append(i)                    
                valor_f.append(c)                 #se almacena el conteo en valor_f
                print(c,"destino encontrado",i,r)
                estado=2                          #se setea estado a 1 para evitar que se repita el valor
                s=1                               #s=1 para ajustar la notificacion al final
            else:
                m[c].append(r)                    #en caso que no haya coincidencias 
                m[c].append(i)                    #se añade a m para su proceso posterior
            c=c+1                                 #contador para que se almacene en distintas direcciones de m
if estado==0:                                     #si no se detecto el destino 
    for i in dt:                                  #creamos un for para leer dt
        for e in m:                               #creamos un for para leer m
            if i[0]==e[0][1]:                     #si hay coincidencias entre el primer valor de i y el segundo valor de e
                if i.count(destino)>0:            #si destino esta en i 
                    print(c1,"encontrado",e[1],e[0],i)
                    estado=1                      #se setea estado a 1 para evitar que se repita el valor
                    m[c1-1].append(i)             #se añade a m
                    valor_f.append(c1-1)          #se añade el contador a valor_f
                c1=c1+1                           #contador

if valor_f.count(0)>0:                            #si en valor_f hay un 0 
    for i in m1:                                  #creamos un bucle para leer m1
        v1=v1+i[2]                                #se suman las horas de viajes
else:                                             #de lo contrario 
    v1=100                                        #se setea v1=100

if valor_f.count(1)>0:                            #si en valor_f hay un 1
    for i in m2:                                  #creamos un bucle para leer m2
        v2=v2+i[2]                                #se suman las horas de viajes
else:                                             #de lo contrario
    v2=100                                        #se setea v2=100

if valor_f.count(2)>0:                            #si en valor_f hay un 2
    for i in m3:                                  #creamos un bucle para leer m3
        v3=v3+i[2]                                #se suman las horas de viajes
else:                                             #de lo contrario
    v3=100                                        #se setea v3=100

if valor_f.count(3)>0:                            #si en valor_f hay un 3
    for i in m4:                                  #creamos un bucle para leer m4
        v4=v4+i[2]                                #se suman las horas de viajes
else:                                             #de lo contrario
    v4=100                                        #se setea v4=100

if valor_f.count(4)>0:                            #si en valor_f hay un 4
    for i in m5:                                  #creamos un bucle para leer m1
        v5=v5+i[2]                                #se suman las horas de viajes
else:                                             #de lo contrario
    v5=100                                        #se setea v5=100
total.append(v1)                                  #se añaden los valores a la lista total
total.append(v2)
total.append(v3)
total.append(v4)
total.append(v5)

if min(total)==100:                               #si el minimo es 100 quiere decir que no hay valores
    print("la ruta es imposible")
else:                                             #de lo contrario
    if s==1:                                      #si s=0 se ajustan los contadores
        print("la mejor ruta es la opcion",total.index(min(total)),"con un total de",total[total.index(min(total))],"horas de viaje")
    else:
        print("la mejor ruta es la opcion",total.index(min(total))+1,"con un total de",total[total.index(min(total))],"horas de viaje")
    

