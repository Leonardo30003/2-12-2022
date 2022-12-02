#Crear un script que indique si el usuario es mayor de edad, menor de edad o es parte de la tercera edad. 
edadUsuario=int(input("Ingrese su edad "))
if edadUsuario>18 and edadUsuario<49:
    print("Es mayor de edad")
elif edadUsuario>50 and edadUsuario<120 :
    print("Es tercera edad")
elif edadUsuario>120:
    print("Fuera de rango")
else:
    print("Es menor de edad")