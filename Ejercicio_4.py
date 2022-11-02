#Un bucle en donde vamos a mezclar operadores logicos e imporima un resultado condicional

#x = "9"
#if (type(x) is int ):
#    print("Es entero")
#    if x>0:
#        print ("El número es par")
#    elif(x==0):
#        print ("x es 0")
#    else:
#        print ("x es menor")
#else:
#    print ("No es entero")

#Puedan incluir libremente un operador lógico = a crear un programa donde le pidan al usuario 
#una condicion lógica para que le entre un resultado de acuerdo

print ("Entradas a un concierto para mayores de edad")

x = "18"

if (type(x) is int ):
    print ("Puedes entrar al concierto")
    if x>=18:
        print ("Tienes la edad requerida para entrar")
    elif x<18:
        print ("Eres menor de edad, no puedes ingresar")
    if x>=80:
        print ("Puede ingresar, pero se le solicitará el carnet de la EPS")
else:
    print ("No puedes entrar al concierto")
