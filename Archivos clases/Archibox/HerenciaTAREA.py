
#Juan Diego Arias 
"""Se modifican los métodos que hemos utilizado al inicio del semestre 
para operaciones con vectores"""


import random as rd

class Dim2:
    def __init__(self, x=0, y=0):
        """
        Constructor de la clase Dim2 que inicializa las componentes x e y del vector.

        Args:
            x (int): Componente x del vector (default 0).
            y (int): Componente y del vector (default 0).
        """
        self.x = x
        self.y = y
    
    @classmethod
    def random_vector(cls):
        """
        Genera un vector aleatorio en Dim2.

        Returns:
            Dim2: Un objeto Dim2 con componentes x e y aleatorias.
        """
        return cls(rd.randint(0, 100), rd.randint(0, 100))
    
    def __getitem__(self, i):
        """
        Obtiene la i-ésima componente del vector.

        Args:
            i (int): Índice de la componente (1 para x, 2 para y).

        Returns:
            int: Valor de la i-ésima componente.
        """
        comp = [self.x, self.y]
        
        if i < 1 or i > 2:
            return "error de indice"
        else:
            return comp[i - 1]
    
    def __add__(self, other):
        """
        Suma dos vectores de Dim2.

        Args:
            other (Dim2): Otro objeto Dim2.

        Returns:
            Dim2: Resultado de la suma de los dos vectores.
        """
        return Dim2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """
        Resta dos vectores de Dim2.

        Args:
            other (Dim2): Otro objeto Dim2.

        Returns:
            Dim2: Resultado de la resta de los dos vectores.
        """
        return Dim2(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        """
        Representación en cadena del vector.

        Returns:
            str: Representación del vector en formato "(x, y)".
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def sum_of_squares(self):
        """
        Calcula la suma de los cuadrados de las componentes del vector.

        Returns:
            int: Suma de los cuadrados de las componentes.
        """
        return self.x ** 2 + self.y ** 2
    
    def magnitude(self):
        """
        Calcula la magnitud del vector en Dim2.

        Returns:
            float: Magnitud del vector.
        """
        return self.sum_of_squares() ** (1 / 2)
    
    def __mul__(self, other):
        """
        Realiza el producto punto entre dos vectores de Dim2.

        Args:
            other (Dim2): Otro objeto Dim2.

        Returns:
            int: Producto punto de los dos vectores.
        """
        return self.x * other.x + self.y * other.y


class Dim3(Dim2):
    def __init__(self, x=0, y=0, z=0):
        """
        Constructor de la clase Dim3 que inicializa las componentes x, y y z del vector.

        Args:
            x (int): Componente x del vector (default 0).
            y (int): Componente y del vector (default 0).
            z (int): Componente z del vector (default 0).
        """
        super().__init__(x, y)
        self.z = z
    
    def __getitem__(self, i):
        """
        Obtiene la i-ésima componente del vector.

        Args:
            i (int): Índice de la componente (1 para x, 2 para y, 3 para z).

        Returns:
            int: Valor de la i-ésima componente.
        """
        comp = [self.x, self.y, self.z]
        
        if i < 1 or i > 3:
            return "error de indice"
        else:
            return comp[i - 1]
    
    def __str__(self):
        """
        Representación en cadena del vector.

        Returns:
            str: Representación del vector en formato "(x, y, z)".
        """
        return super().__str__()[:-1] + "," + str(self.z) + ")"
    
    def __add__(self, other):
        """
        Suma dos vectores de Dim3.

        Args:
            other (Dim3): Otro objeto Dim3.

        Returns:
            Dim3: Resultado de la suma de los dos vectores.
        """
        return Dim3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """
        Resta dos vectores de Dim3.

        Args:
            other (Dim3): Otro objeto Dim3.

        Returns:
            Dim3: Resultado de la resta de los dos vectores.
        """
        return Dim3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def sum_of_squares(self):
        """
        Calcula la suma de los cuadrados de las componentes del vector.

        Returns:
            int: Suma de los cuadrados de las componentes.
        """
        return super().sum_of_squares() + self.z ** 2
    
    def magnitude(self):
        """
        Calcula la magnitud del vector en Dim3.

        Returns:
            float: Magnitud del vector.
        """
        return self.sum_of_squares() ** (1 / 2)
    
    def __mul__(self, other):
        """
        Realiza el producto punto entre dos vectores de Dim3.

        Args:
            other (Dim3): Otro objeto Dim3.

        Returns:
            int: Producto punto de los dos vectores.
        """
        return super().__mul__(other) + self.z * other.z
    
    @classmethod
    def random_vector(cls):
        """
        Genera un vector aleatorio en Dim3.

        Returns:
            Dim3: Un objeto Dim3 con componentes x, y y z aleatorias.
        """
        return cls(rd.randint(0, 100), rd.randint(0, 100), rd.randint(0, 100))


# Impresiones

x = Dim2.random_vector()
y = Dim3.random_vector()

print(x)
print(x.magnitude(), "\n")

print(y)
print(y.magnitude(), "\n")

print(x + y)
print(x - y)
print(x * y)




