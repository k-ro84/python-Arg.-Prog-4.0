a = True
b = False

print(a and a)  #True and True
print(a and b)  #True and False

print("--------------------")

print(a or b)  #True or False  como tenemos al menos un verdadero el resultado es verdadero

print(b or b)  #False or False

print("--------------------")

print((3<4)and(4<5)) #T y T -->True

print((3<4)and(6<5)) #T y F -->False

print("--------------------")
#Negacion  --->not

resultado = a and a #True and True
#print(resultado)
print(not resultado)

resultado = a and b #True and False
#print(resultado)
print(not resultado)