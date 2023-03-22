import math as ma

class RungeKutta:
    def __init__(self, x0, y0, xn, N):
        self.x0 = x0
        self.y0 = y0
        self.xn = xn
        self.N = N
        self.h = (xn - x0) / N

    def f(self, x, y):
        return x * y + x ** 3
#funcion de la forma dy/dx = f(x,y)
#algunas ED recomnedadas son: 
# dy/dx=-2*x+y*x,                   1≤x≤2,    y(1)=-3   y  N=5
# dy/dx=-2*ma.exp(-xy) ,            0≤x≤3 ,   y(0)=1    y  N=10
# dy/dx=-2*ma.cos(2x)+ma.sin(y),   -2≤x≤-1,   y(-1)=0   y  N=10
# dy/dx=1+y/x,                   -2.5≤x≤-0.5, y(-2.5)=1 y  N=10
# dy/dx=5*x**2-3*x+ma.exp(-x),     2≤x≤4,    y(2)=2    y  N=15
    def runge_kutta(self):
        x = self.x0
        y = self.y0
        for i in range(self.N):
            k1 = self.h * self.f(x, y)
            k2 = self.h * self.f(x + self.h / 2, y + k1 / 2)
            k3 = self.h * self.f(x + self.h / 2, y + k2 / 2)
            k4 = self.h * self.f(x + self.h, y + k3)
            y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x += self.h
        return y

    def error(self):
        y_exacta = 2*ma.exp(self.xn**2/2) - self.xn**2 - 2
        y_aproximada = self.runge_kutta()
        orden_error = (self.h)**4 
        error = abs(y_exacta - y_aproximada)
        return y_exacta,error, orden_error

# Ejemplo de uso:
rk = RungeKutta(x0=0, y0=0, xn=1, N=10)
y_aproximada = rk.runge_kutta()
y_exacta, error, orden_error = rk.error()
print("Resuelve una ecuacion diferencial de la forma dy/dx=x*y+x**3,\
 sujeto a y(0)=0.5, con xn entre 0 y 2, N=10")
#print(f"Valor exacto de y(x_n) = {y_exacta:.6f}")
print(f"Valor aproximado de y(x_n) = {y_aproximada:.6f}")
#print(f"Error del metodo de orden h^4 = {error:.6f}")
print(f"Error del orden h^4 = {orden_error:.6f}")
