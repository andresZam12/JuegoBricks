import random

number = random.randint(1, 10)
guess = int(input("Adivina el número (1-10): "))
if guess == number:
    print("¡Correcto!")
else:
    print(f"¡Incorrecto! Era {number}.")
