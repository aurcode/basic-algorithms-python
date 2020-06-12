
#  Enumeración exhaustiva
def enumerado(objetivo):
	respuesta = 0
	while respuesta**2 < objetivo:
	    respuesta += 1

	if respuesta**2 == objetivo:
	    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
	else:
	    print(f'{objetivo} no tiene una raiz cuadrada exacta')

#  Aproximación de soluciones
def aproximacion(objetivo):
	epsilon = 0.01
	paso = epsilon**2 
	respuesta = 0.0

	while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
	    respuesta += paso

	if abs(respuesta**2 - objetivo) >= epsilon:
	    print(f'No se encontro la raiz cuadrada {objetivo}')
	else:
	    print(f'La raiz cudrada de {objetivo} es {respuesta}')

#  Búsqueda binaria
def busqueda_binaria(objetivo):
	epsilon = 0.0000000000001
	bajo = 0.0
	alto = max(1.0, objetivo)
	respuesta = (alto + bajo) / 2

	while abs(respuesta**2 - objetivo) >= epsilon:
	    if respuesta**2 < objetivo:
	        bajo = respuesta
	    else:
	        alto = respuesta

	    respuesta = (alto + bajo) / 2

	print(f'La raiz cuadrada de {objetivo} es {respuesta}')


# Interfaz
print("""
		Bienvenido

		Para encontrar la raíz cuadrada escoge uno de los siguientes algoritmos:

		1) Enumeración exhaustiva
		2) Aproximación de soluciones
		3) Búsqueda binaria
		""")

# Seleccion de algoritmo
algoritmo = int(input('¿Cual algoritmo quieres utilizar? (1, 2 o 3): '))

if algoritmo == 1:
	print("Usted ha escogido Enumeración exhaustiva")
	enumerado(int(input("Escoge un entero: ")))
elif algoritmo == 2:
	print("Usted ha escogido Aproximación de soluciones")
	aproximacion(int(input("Escoge un entero: ")))
elif algoritmo == 3:
	print("Usted ha escogido Búsqueda binaria")
	busqueda_binaria(int(input("Escoge un entero: ")))
else:
	print("Opción incorrecta, reinicie el programa")
