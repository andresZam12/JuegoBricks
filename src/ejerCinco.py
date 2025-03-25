import random
import time

num1, num2 = random.randint(1, 10), random.randint(1, 10)
start = time.time()
answer = int(input(f"¿Cuánto es {num1} + {num2}? "))
end = time.time()

if answer == num1 + num2:
    print(f"¡Correcto! Tiempo: {end - start:.2f} segundos.")
else:
    print(f"¡Incorrecto! Era {num1 + num2}.")
