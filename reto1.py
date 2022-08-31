# entrada = variables=referencias en memoria
nivelAgua=int(input("Digite el nivel de agua"))



#proceso
if(nivelAgua>=0 and nivelAgua<20):
    #salida
    print(f'el nivle de agua es {nivelAgua}  y este es bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    #salida
    print(f'el nivle de agua es {nivelAgua}  operando normalmente')
elif(nivelAgua>400):
    #salida
    print(f'el nivle de agua es {nivelAgua}  llame a fico y lupe')
else:
    #salida
    print("El nivel de agua no es valido")

