secret = "python"
guess = input("Adivina la palabra secreta: ").lower()

if guess == secret:
    print("¡Correcto!")
else:
    print("Intenta de nuevo.")
