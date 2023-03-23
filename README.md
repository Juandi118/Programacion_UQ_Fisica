# Programacion_UQ_Fisica
# Juan Diego Arias Iguita_Primer parcial 
## Se crea un código de aproximación de solución de ecuaciones diferenciales o PVI con el método de rugen-kutta de orden 4 (RK4)
[![RK4.png](https://i.postimg.cc/CMQB7cT0/RK4.png)](https://postimg.cc/0r7y2dyX)

además h estás dado por $h=\dfrac{(x_n-x_0)}{N}$, donde $N$ son el número de aproximaciones sucesivas, en la imagen $t_i=x_0$, solo es una variación en la notación del método. El error del método es del órden de $h^4$.

En python creamos un clase RungeKutta donde se definen los parametros del método. 
Se define una función que cumpla la forma $\dfrac{dy}{x}=f(x,y)$ en el que definimos $f(x,y)$ 
Luego se hace un ciclo para tener definidos los valores de $k_1, k_2, k_3, k4, x$ para obtener la aproximación a la solución de la ED dada por $y$
