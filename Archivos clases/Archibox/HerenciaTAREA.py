
#Juan Diego Arias 
"""Se modifican los métodos que hemos utilizado al inicio del semestre 
para operaciones con vectores"""

import random as rd
class dim2:
  def __init__ (self,x=0,y=0):
    self.x = x
    self.y = y
  
  def ran_vec(self): #Metodo para generar un vector random 
   return dim2(rd.randint(0,100), rd.randint(0,100))

  def __getitem__(self,i): #metodo 1 de la clase padre, retorna la componente según su posición
    comp = [self.x,self.y]

    if i<1 or i>2:
      return "error de indice"
    else:
      return comp[i-1]

  def __add__ (self, otro): #metodo 2 dunder de la clase padre para sumar vectores definido con "+"  
    return dim2(self.x + otro.x, self.y + otro.y)

  def __sub__ (self, otro): #metodo 3 dunder de la clase padre para restar vectores definido con "-"  
    return dim2(self.x - otro.x, self.y - otro.y)
  
  def __str__(self): #método 4 de la clase padre 
    return ("("+str(self.x)+","+str(self.y)+")")
  
  def suma_cuadrados(self):
    return (self.x**2 +self.y**2)

  def magnitud(self): #magnitud del vector en R2 usando el metodo de suma de cuadrados
    return self.suma_cuadrados()**(1/2)
  
  def __mul__(self,otro): # dot product
    return self.x*otro.x + self.y*otro.y



# Se crea la clase hijo o vectores en R3
class dim3(dim2):
  def __init__(self,x=0,y=0,z=0):
    super().__init__(x,y) #se hereda el constructor de la clase padre (dim2) y se agrega la componente z para crear un vector en R3
    self.z = z
  
  def __getitem__(self,i): #metodo 1 de la clase padre, retorna la componente según su posición
    comp = [self.x,self.y]

    if i<1 or i>3:
      return "error de indice"
    else:
      return comp[i-1]

  def __str__(self): # se hereda el metodo para la impresion de vectores en R2 de la clase dim2
    return super().__str__()[:-1] + "," + str(self.z)+")"

  def __add__(self,otro): #se dedine metodo dunder para sumar vectores de dimensión 3
    return dim3(self.x + otro.x, self.y + otro.y, self.z + otro.z)

  def __sub__(self,otro): #se dedine metodo dunder para restar vectores de dimensión 3
    return dim3(self.x - otro.x, self.y - otro.y, self.z - otro.z)

  def suma_cuadrados(self): #Se hereda el metodo de la suma de cuadrados de dim2
    return super().suma_cuadrados()+self.z**2

  def magnitud(self): # se saca raiz a a la suma de cuadrados de un vector en R3 
    return self.suma_cuadrados()**(1/2)

  def __mul__(self,otro): #producto punto para R2
    return super().__mul__(otro) + self.z*otro.z

  def ran_vec(self): #Metodo para generar un vector random, no se hace un for para que no quede un type tuple
   return dim3(rd.randint(0,100), rd.randint(0,100), rd.randint(0,100))


  
#impresiones

x = dim2()
y = dim3()

x = x.ran_vec()
y = y.ran_vec()

print(x)
print(x.magnitud(), "\n")

print(y)
print(y.magnitud(),"\n")


print(x+y)

print(x-y)

print(x*y)



