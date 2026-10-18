secret = 27
guesses = [10, 35, 20, 27, 40]

for guess in guesses:
    if guess == secret:
        print("Correct guess!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print("Game over")