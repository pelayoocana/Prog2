import random

def numero_secreto():
    minimo = 10
    maximo = 30
    numero_intentos = 5

    print(f"Tienes un número máximo de {numero_intentos} intentos.")
    secret_number = random.randint(minimo, maximo)

    for intentos in range(numero_intentos):
        numero = int(input("Introduce un número: "))  # Fixed the input prompt message.

        if numero == secret_number:
            print(f"¡Vaya, adivinaste! El número es {secret_number}")
            break  # You should break out of the loop when the number is guessed correctly.
        elif numero > secret_number:
            print("El número es mayor. Prueba uno más chico.")
        else:
            print("El número es menor. Prueba uno más grande.")

    else:
        print(f"Lo siento, has agotado tus {numero_intentos} intentos. El número secreto era {secret_number}")

numero_secreto()
