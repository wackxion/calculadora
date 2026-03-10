class calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: sero no se divide"

f = calculadora(23, 5)

print(f.suma(f.a, f.b))
print(f.resta(f.a, f.b))
print(f.multiplicacion(f.a, f.b))
print(f.dividir(f.a, f.b))




        
