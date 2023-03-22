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
        error = abs(y_exacta - y_aproximada)
        return y_exacta,error

# Ejemplo de uso:
rk = RungeKutta(x0=0, y0=0, xn=1, N=10)
y_aproximada = rk.runge_kutta()
y_exacta, error = rk.error()
print(f"Valor exacto de y(x_n) = {y_exacta:.6f}")
print(f"Valor aproximado de y(x_n) = {y_aproximada:.6f}")
print(f"Error del método de orden h^4 = {error:.6f}")