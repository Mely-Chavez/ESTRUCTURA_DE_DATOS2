#Listas Práctica 1
Itic3=["Eduardo Flores", "Nidia Vanessa Chávez Rendón", "Sajith Alexandro", 
"Emmanuel de Jesús Esparza", "Melany Chávez", "Fernanda Pantoja", "Jonathan de Jesús", "Santiago Herrera"]
Carreras_ITPA = ["TICs", "Mecatrónica", "Gestión Empresarial", "Lógistica", "Industrial"]
Edades = [18, 18, 19, 20, 20, 19, 19, 18, 19, 19, 19, 19]

#Imprimir lista
print(Itic3)
print(Carreras_ITPA)
print(Edades)

#Imprimir el tercer campo  cada lista
print(Carreras_ITPA[2])

#Agregar elemento al final de la lista
Itic3.append('Nidia Vanessa Chávez Rendón')
print(Itic3)

#Agregar otra lista
Itic3.extend(['Vanessa', 'Juan'])
print(Itic3)

#Agregar elemento en la posición 5
Itic3.insert(4, "Rainer")
print(Itic3)

#Borra un valor determinado
del Edades[0]
print(Edades)

#Ver el tamaño de nuestras listas
print(len(Edades))
print(len(Itic3))
print(len(Carreras_ITPA))

#Eliminar un elemento en específico
Edades.remove(32)
print(Edades)

#Ordenar elementos
print(Edades)
print("")
Edades.sort()
print(Edades)