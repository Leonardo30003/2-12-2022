#Haz una tabla de multiplicar utilizando el ciclo for.
tabla_desde = 1 
tabla_hasta = 10 
desde = 1 
hasta = 10 

for numeroTabla in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {numeroTabla}:')
	for valorMultiplicar in range(desde, hasta + 1):
		print(f'{numeroTabla} x {valorMultiplicar} = {numeroTabla * valorMultiplicar}')
