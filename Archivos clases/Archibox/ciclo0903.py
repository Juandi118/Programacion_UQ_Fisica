for i in range(4): 
    print((i+1)*"x")

for i in range(4):
    print("Paco "*(i+1))


for i in range (4):
    print("*"*6)


for i in range (4):
    print("*"*(i+1))

for i in range (4):
    print("*"*(4-i))


#Pequeño programa para dterminar dinero 
x = float(input("Ingrese la cantidad de dinero que desea poner en el CDT: "))
N = int(input("¿Cuantos años dejará el dinero? "))
p = float(input("ingrese el porcentaje de interés pactado (solo el numero): "))
for i in range (N):
    x = x*(1*p/100)
print("Despues de {0} años, usted tendrá {1}".format(N,x))

#
num = int(input("ingrese numero positivo: "))
while num <= 0:
    num = int(input("POSITIVO: "))
    


# num = eval(input("Ingrese un número: "))

#agrego commit



while True:
    temp = float(input("Ingrese una temperatura en Celcius para pasar a Fahrenheit (-1000 para salir): "))
    if temp == -1000:
        print("Bye")
        break
    print("Tu temperatura equivale a {}°F".format(9/5*temp+32))





for i in range (10):
    num = float(input("Ingrese un numero: "))
    if num<0:
        print("ERROR: Número negativo")
        break 
else:
    print("El usuario introdujo los 10 valores")  
          