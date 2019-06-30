import random

my_number = random.randint(0, 20)

guess = -1

trials = 0

print("Guess mu number")

while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print("Congratulations, you are right! You guessed after", trials, "attempts")
    elif guess > my_number:
        trials += 1
        print("Sorry - my number is smaller than your guess. Yours numbers of trials: ", trials)
    else:
        trials += 1
        print("Sorry - my number is greater than your guess. Yours numbers of trials ", trials)

number = 1
previous_number = 0

while number <= 50:
    print(number + previous_number)
    previous_number = number
    number += 1
