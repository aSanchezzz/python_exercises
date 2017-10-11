secret_num = 5

print("I am thinking of a number between 1 and 10")

while True:
    guess = int(input("What's the number? "))
    if guess == secret_num:
        print("Yes, you win!")
        break
    else:
        if guess < secret_num:
            print("{} is too low.".format(guess))
        if guess > secret_num:
            print("{} is too high.".format(guess))
