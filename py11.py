# Secret number
secret_number = 7

# Start guessing loop
while True:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Try again!")
