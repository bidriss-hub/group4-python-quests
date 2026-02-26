secret_code = 42
attempts = 0

while attempts < 3:
    guess = int(input("Enter the secret code: "))
    if guess == secret_code:
        print("Correct! You broke the code.")
        break
    else:
        print("Wrong code.")
        attempts += 1

if attempts == 3 and guess != secret_code:
    print("Game over. You failed to guess the code.")