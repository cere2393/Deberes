#Cree un programa en python que solicite la cantidad de temperaturas que desea ingresar,
# después cree una lista para almacenar cada una 
# de las temperaturas que indicó el usuario que ingresaría, 
# luego solicite al usuario cada una de las temperaturas que se deberán ingresar en la lista.
#Con los valores previamente ingresados a la lista se desea calcular 
#su media y determinar entre todas ellas cuantas son superiores o iguales a esa media.

#cantidad_temperaturas = int(input("¿Cuántas temperaturas desea ingresar? "))

#temperaturas=[]


 # Solicitar la cantidad de temperaturas a ingresar
cantidad_temperaturas = int(input("¿Cuántas temperaturas desea ingresar? "))
    
    # Crear una lista para almacenar las temperaturas
temperaturas = []
    
    # Solicitar al usuario cada una de las temperaturas
for i in range(cantidad_temperaturas):
  temperatura = float(input("Ingrese la temperatura #{0}: ".format(i + 1)))
temperaturas.append(temperatura)
    
    # Calcular la media de las temperaturas
suma = sum(temperaturas)
media= suma/cantidad_temperaturas
    
    # Contar cuántas temperaturas son superiores o iguales a la media
conteo_superiores_o_iguales =  >= media)
    
    # Mostrar los resultados 
print("La media de las temperaturas es:",media)
print("Cantidad de temperaturas superiores o iguales a la media: ",conteo_superiores_o_iguales)
