# Juan Diego Arias & David Sebastian Rivera

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
            
        
 #definir matrices 2x2       

class matriz:
    def __init__ (self, matriz):
        self.matriz = matriz 

    def __str__(self):
        respuesta = "| "+str(self.matriz[0][0])+"  "+str(self.matriz[0][1])+" |\n| "+str(self.matriz[1][0])+"  "+str(self.matriz[1][1])+" |"
        return(respuesta)
    
    #Defino suma
    def __add__(self, otra):
        nueva_matriz = [ [self.matriz[0][0]+otra.matriz[0][0], self.matriz[0][1]+otra.matriz[0][1]], 
                        [self.matriz[1][0]+otra.matriz[1][0], self.matriz[1][1]+otra.matriz[1][1]]]
        return(matriz(nueva_matriz))
    
    #Defino resta
    def __sub__(self, otra):
        nueva_matriz = [ [self.matriz[0][0]-otra.matriz[0][0], self.matriz[0][1]-otra.matriz[0][1]], 
                        [self.matriz[1][0]-otra.matriz[1][0], self.matriz[1][1]-otra.matriz[1][1]]]
        return(matriz(nueva_matriz))
    
    #Defino multiplicación
    def __mul__(self, numero):
        nueva_matriz = [[self.matriz[0][0]*numero, self.matriz[0][1]*numero],
                        [self.matriz[1][0]*numero, self.matriz[1][1]*numero]]
        return(matriz(nueva_matriz))
    
    def __rmul__(self, numero):
        nueva_matriz = [[numero*self.matriz[0][0], numero*self.matriz[0][1]],
                        [numero*self.matriz[1][0], numero*self.matriz[1][1]]]
        return(matriz(nueva_matriz))
    

    def columna_i(self, indice):
        respuesta = "|"+str(self.matriz[0][indice])+"|\n|"+str(self.matriz[1][indice])+"|"
        return(respuesta)
    #return [self.matriz[0][indice], self.matriz[1][indice]]




#Operaciones con vectores
print("Operaciones con vectores",sep="",end="\n\n")
v1 = vector(1,2,3)
v2 = vector(2,6,9)

print(v1)
print(v2,sep="",end="\n\n")
print(v1+v2,sep="",end="\n\n")
print(v1-v2,sep="",end="\n\n")
print(v1*v2,sep="",end="\n\n")
#print(v2*v1)
print(v2*2,sep="",end="\n\n")
#print(2*v2)


#Operaciones con matrices
print("Operaciones con matrices",sep="",end="\n\n")
A = matriz([[1,2],[3,4]])
B = matriz([[1,2],[3,4]])

print(A,sep="",end="\n\n")

print(B,sep="",end="\n\n")

print(A+B,sep="",end="\n\n")

print(A-B,sep="",end="\n\n")

print(A*3,sep="",end="\n\n")

print(A.columna_i(0),sep="",end="\n\n")

print(A.columna_i(1),sep="",end="\n\n")



#print(3*A,sep="",end="\n\n")







