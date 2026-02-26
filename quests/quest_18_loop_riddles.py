secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number: "))
print("Correct! You found the secret number.")