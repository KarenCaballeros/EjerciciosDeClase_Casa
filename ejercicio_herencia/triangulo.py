from ejemploHerencia import FiguraGeometrica

class Triangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		super(). __init__(base, altura)
	def imprimir(self):
		resultado= ""
		for i in range(1, self.altura + 1):
			esp= self.altura-i
			resultado += ("  "* esp, "*" * i) + "\n"			
		return resultado
	def calcular(self):
		return super().calcular_area() / 2.0	
