import random
secret_number = random.randint(1,10)
guess = int(input("Guess the number: "))
if guess == secret_number:
    print("Correct number")
elif guess < secret_number:
    print("Too low")
else:
    print("Too High")