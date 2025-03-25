import random

player = random.randint(1, 6)
computer = random.randint(1, 6)

print(f"Tú tiraste {player}, la computadora tiró {computer}.")
if player > computer:
    print("¡Ganaste!")
elif player < computer:
    print("¡Perdiste!")
else:
    print("Empate.")
