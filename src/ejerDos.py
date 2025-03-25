import random

choices = ["piedra", "papel", "tijera"]
computer = random.choice(choices)
player = input("Elige piedra, papel o tijera: ").lower()

if player == computer:
    print(f"Empate, ambos eligieron {computer}.")
elif (player == "piedra" and computer == "tijera") or \
     (player == "papel" and computer == "piedra") or \
     (player == "tijera" and computer == "papel"):
    print(f"¡Ganaste! {player} vence a {computer}.")
else:
    print(f"¡Perdiste! {computer} vence a {player}.")
