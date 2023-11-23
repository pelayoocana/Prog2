import random

def main():
    # set the range of numbers and the numbers of attemps 
    min_number = 3
    max_number=23
    max_attemps=4

# si poenmos un breakpoint y hacemos debug donde esta puesto en el secret_number, podemos ver cual es el nnumero aantes de hacer el juego completo 

    # generate a random number for the playe to guess
    secret_number = random.randint(min_number, max_number)

    print(f"Welcome to guess the number!!")
    print(f"Im thinking a number between {min_number} and {max_number}")

    for attempt in range(1, max_attemps):
        guess=int(input((f"Attempt{attemp}")))
        print(f"callate tonto y estudia")

