import random

def guess_the_number():
    name = input("Привет! Как вас зовут?\n")
    print(f"\nНу, {name}, я загадал число от 1 до 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Попробуйте угадать.\n"))
        attempts += 1

        if guess < secret_number:
            print("Выше")
        elif guess > secret_number:
            print("Ниже")
        else:
            print(f"Отличная работа, {name}! Вы угадали мой номер с {attempts} попыток!")
            break

guess_the_number()