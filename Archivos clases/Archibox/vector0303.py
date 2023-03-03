class vector:
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y
        self.z = z
        self.magnitud = (self.x**2+self.y**2+self.z**2)**0.5
 #Notación para imprimir respuesta
    def __str__(self):
        respuesta = "["+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+"]"
        return(respuesta)
#suma
    def __add__(self,otro):
        x = self.x + otro.x
        y = self.y + otro.y
        z = self.z + otro.z
        return(vector(x,y,z))
#resta
    def __sub__(self,otro):
        x = self.x - otro.x
        y = self.y - otro.y
        z = self.z - otro.z
        return(vector(x,y,z))
#producto punto y producto por escalar
    def __mul__(self,otro):
        if (type(self)==type(otro)):
             resultadoescalar= self.x*otro.x + self.y*otro.y + self.z*otro.z
             return(resultadoescalar)
        else:
            return(vector(self.x*otro, self.y*otro, self.z*otro))

# definir multiplicacion por el otro lado 
    def __rmul__(self,otro):
        if (type(self)==type(otro)):
             resultadoescalar= otro.x*self.x + otro.y*self.y + otro.y*self.z
             return(resultadoescalar)
        else:
            return(vector(otro*self.x, otro*self.y, otro*self.z))



# impresiones 
v1 = vector(1,2,3)
v2 = vector(2,6,9)
v3 = v1+v2

print(v1)
print(v2)
print("numero entero:", 2)

print("suma:",v3)
print("resultado de la multiplicacion entre dos vectores (right):", v1*v2)
print("resultado de la multiplicacion entre dos vectores:", v2*v1)
print("resultado de la multiplicacion por un entero (right):", v2*2)
print("resultado de la multiplicacion por un entero:", 2*v2)





