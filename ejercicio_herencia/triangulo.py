from ejemploHerencia import FiguraGeometrica

class Triangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		super(). __init__(base, altura)
	def imprimir(self):
		cont = self.altura
		resultado = ""
		while cont > 0:
			for i in range(0, self.altura):
				resultado += (" "*(self.altura-i-1) + "* " * (i+1) + "\n")
				cont = cont - 1
		return resultado	
	def calcular_area(self):
		return super().calcular_area() / 2.0	
