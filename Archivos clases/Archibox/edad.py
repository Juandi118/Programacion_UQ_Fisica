edad = int(input("Por favor digite su edad en números: "))
mes = int(input("Ingrese su mes de nacimiento (en números): "))
if edad >= 0:
    if mes <=12 and mes > 0:
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad") 
    else:
        print("No es un mes del calendario gregoriano")
else:
    print("QUÉ??")                  


