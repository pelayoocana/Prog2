import random 

def numero_secreto():
    minimo=10
    maximo=30
    numero_intentos=5

    print(f"Tienes un numero máximo de {numero_intentos}")
    secret_numer=random.randint(minimo,maximo)

    for intentos in range(minimo, maximo+1):
        numero=int(input("Introduce un numero bb"))
        if numero==secret_numer:
            print(f"Vaya, adivinaste el  numero es{secret_numer}")
        elif numero>secret_numer:
            print("El numero es mayor, prubea uno mas chico")
        else:
            print("El numero es menol brdel ")
    
return numero_secreto()


        