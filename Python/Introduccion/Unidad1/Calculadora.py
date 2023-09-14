print ("Calculadora.")
n1 = float(input("Escribe un primer número: ") )
n2 = float(input("Escribe un segundo núnmero: ") )

opcion = 0
while True:
    print("""¿Qué quieres hacer con los números?
    
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir de la calculadora
    """)
    opcion = int(input("Menú: ") )     

    if opcion == 1:
        print(" ")
        print("El resultado de sumar: ",n1,"+",n2," es igual a: ",n1+n2)
    elif opcion == 2:
        print(" ")
        print("El resultado de restar: ",n1,"-",n2," es igual a: ",n1-n2)
    elif opcion == 3:
        print(" ")
        print("El resultado de multiplicar: ",n1,"*",n2," es igual a: ",n1*n2)
    elif opcion == 4:
        print(" ")
        print("El resultado de dividir: ",n1,"/",n2," es igual a: ",n1/n2)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")