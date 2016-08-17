from cuadrado import Cuadrado
from triangulo import Triangulo

menu_principal = 1

while menu_principal == 1:

	menu_principal = int(input("""
*Menu principal*
1. Crear figura.
2. Salir.
Ingrese opcion elegida: """))

	if menu_principal == 1:

		menu_2 = int(input("""
Que desea crear?
1. Cuadrado.
2. Triangulo.
Ingrese opcion elegida: """))

		if menu_2 == 1:
			print("")
			lado = int(input("ingrese la medida de un lado: ")) 
			mi_cuadrado = Cuadrado(lado)
			eleccion = int(input("""
Desea...
1. Area.
2. Imprimir figura.
Ingrese la opcion elegida: """))

			if eleccion == 1:
				print("")
				print("Area: " , mi_cuadrado.calcular_area())
			elif eleccion == 2:	
				print("")
				print(mi_cuadrado.imprimir())

		elif menu_2 == 2:
			print("")
			base = int(input("ingrese la medida de la base: "))
			altura = int(input("ingrese la medida de la altura: ")) 
			mi_triangulo = Triangulo(base, altura)
			eleccion = int(input("""
Desea...
1. Area.
2. Imprimir figura.
Ingrese la opcion elegida: """))

			if eleccion == 1:
				print("")
				print("Area: " , mi_triangulo.calcular_area())
			elif eleccion == 2:	
				print("")
				print(mi_triangulo.imprimir())	

		else: 
			print("Opcion invalida.")

print("")
print("Gracias por utilizar Uso_figuras.py , Adios.")
