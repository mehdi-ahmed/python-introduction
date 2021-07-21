secret_number = 8
attempts = 0
guess_limit = 3

while attempts < guess_limit:
    guess = int(input('Guess a number: '))
    attempts += 1
    if guess == secret_number:
        print("Well done !")
        break
else:
    print("Sorry you failed !")
