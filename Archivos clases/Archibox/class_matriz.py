class matriz:
    def __init__(self, valores):
        self.valores = valores
        n = len(list)
        m = len(valores[0])
        self.shape = [n, m]
    def __str__(self):
        if self.shape[0]==1:
           respuesta = self._imprimir_vetor_(0)
           return(respuesta)
        else: 
            respuesta = ""
            for i in range(self.shape[0]-1):
                respuesta = respuesta + self._imprimir_vetor_(i)+"\n"
            respuesta = respuesta + self._imprimir_vetor_(self.shape[0]-1)
            return(respuesta)

    def _imprimir_vetor_(self, fila): 
        respuesta = "|"
        for i in range(self.shape[1]-1):
            respuesta = respuesta + str(self.valores[fila][i])
            respuesta = respuesta + " "

        respuesta = respuesta + str(self.valores[fila][self.shape[1]-1]) + "|" 
        return(respuesta)  
        
    def __add__(self, otro):
        if self.shape[0]==1:
            lista = []
            for i in range(self.shape[1]):
                lista.append(self.valores[0][i]+otro.valores[0][i])
            respuesta = matriz([lista])
            return(respuesta)
        else: 
            matriz = [[0]*self.shape[1]]*self.shape[0]
            ......
            


v1= matriz([[1,2,3],[4,5,6]], 1, 3)
print(v1)








