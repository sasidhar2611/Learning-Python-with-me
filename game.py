import random

num = random.randint(1, 10)


tries = 0

while True:
    guess = int(input("Please guess your number(1 - 10): "))

    if guess == num:
        tries += 1
        print(f"You are right. You guessed the number in {tries} tries.")
        break
    elif num<guess:
        tries += 1
        print("Go a little lower")

    elif num>guess:
        tries += 1
        print("Go a little higher")

    else:
        tries += 1
        print("You are wrong")