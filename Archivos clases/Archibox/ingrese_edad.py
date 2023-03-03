def solicitar_edad():
    edad = int(input("Por favor digite su edad en números: "))
    return edad

def solicitar_mes():
    mes = int(input("Ingrese su mes de nacimiento (en números): "))
    return mes 

def definir_edad():
    edad = solicitar_edad()
    if edad >= 0:
        mes = solicitar_mes()
        if mes <=12 and mes > 0:
            if edad >= 18:
                print("Eres mayor de edad")
            else:
                print("Eres menor de edad") 
        else:
            print("No es un mes del calendario gregoriano")
    else:
        print("QUÉ??")                  

definir_edad()

