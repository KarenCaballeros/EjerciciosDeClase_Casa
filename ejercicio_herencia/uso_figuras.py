from cuadrado import Cuadrado
from triangulo import Triangulo

menu_principal = int(input("""
*Menu principal*
1. Crear figura.
2. Salir.
Ingrese opcio9n elegida: """))

while menu_principal == 1:
	figura_elegida = int(input("""
¿Que desea crear?
1. Cuadrado.
2. Triangulo.
Ingrese opcion elegida: """))
	if figura_elegida == 1:
		lado = int(input("ingrese la medida de un lado: ")) 
		mi_cuadrado = Cuadrado(lado)
		eleccion = int(input("""
Desea...
1. Area.
2. Imprimir figura.
3. Volver al menu principal.
4. Salir.
Ingrese la opcion elegida: """))

		if eleccion == 1:
			print("Area: " , mi_cuadrado.calcular_area())
		elif eleccion == 2:	
			print(mi_cuadrado.imprimir())
		elif eleccion == 3:
			print("")
		elif eleccion == 4:
			print("Gracias por utilizar *USO_FIGURAS.PY, vuelva pront.")
			menu_principal == 2			

	elif figura_elegida == 2:
		base = int(input("ingrese la medida de la base: "))
		altura = int(input("ingrese la medida de la altura: ")) 
		mi_triangulo = Triangulo(base, altura)
		eleccion = int(input("""
Desea...
1. Area.
2. Imprimir figura.
3. Volver al menu principal.
4. Salir.
Ingrese la opcion elegida: """))

		if eleccion == 1:
			print("Area: " , mi_triangulo.calcular_area())
		elif eleccion == 2:	
			print(mi_triangulo.imprimir())	
		elif eleccion == 3:
			print("")
		elif eleccion == 4:
			print("Gracias por utilizar *USO_FIGURAS.PY, vuelva pront.")
			menu_principal == 2		