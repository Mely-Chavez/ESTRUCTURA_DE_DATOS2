## Melany Marlen Chavez Ortiz
#####Frase invertida

def invertir_frase(frase):
    palabras = frase.split()
    palabras_invertidas = palabras[::-1]
    frase_invertida = ' '.join(palabras_invertidas)

    return frase_invertida

frase_original = input("Ingrese una frase: ")
frase_invertida = invertir_frase(frase_original)
print("Frase invertida:", frase_invertida)


### Realizar un programa en el que registre números con colas y pilas. 
### el programa no guardará números repetidos.

cola = []
pila = []

def agregar_cola(numero):
    if numero not in cola:
        cola.append(numero)
        print(f"Agregado {numero} a la cola.")
    else:
        print(f"{numero} en cola.")

def agregar_pila(numero):
    if numero not in pila:
        pila.append(numero)
        print(f"Agregado {numero} a la pila.")
    else:
        print(f"El número {numero} en pila.")

def Cola(): 
    print("Cola:")
    for elemento in cola:
        print(elemento, end=" ")
    print()

def Pila():
    print("Pila:")
    for elemento in reversed(pila):
        print(elemento, end=" ")
    print()

def main():
    while True:
        try:
            opcion = int(input("1. Agregar a la cola\n2. Agregar a la pila\n3. Mostrar cola\n4. Mostrar pila\n5. Salir\nSeleccione una opción: "))
            if opcion == 1:
                numero = int(input("Múmero para la cola: "))
                agregar_cola(numero)
            elif opcion == 2:
                numero = int(input("Número para la pila: "))
                agregar_pila(numero)
            elif opcion == 3:
                Cola()
            elif opcion == 4:
                Pila()
            elif opcion == 5:
                print("Salir.")
                break
            else:
                print("Opción no válida unu.")
        except ValueError:
            print("Ingrese un número válido.")

if _name_ == "_main_":
    main()
