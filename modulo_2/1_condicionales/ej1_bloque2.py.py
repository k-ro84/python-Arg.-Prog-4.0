#age = input(" ingrese su edad por favor: ") # pedido de esta manera lo registra como que pide un string
#por ende seria dato=input("") solicitud de string para que ingrese el usuario desde el front

#para que lo que ingrese sea tomado como un int
age =int(input(" ingrese su edad por favor: "))
if age<18 : #se pone los dos puntos por que forma parte del lenguaje de python tanto en if como en else
    print( " eres menor de edad")
else :
    print( " eres mayor de edad ")
