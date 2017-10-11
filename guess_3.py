import random
rand_num = random.randint(1, 10)

print("I am thinking of a number between 1 and 10")
while True:
    guess = int(input("What's the number? "))
    if guess == rand_num:
        print("Yes, you win!")
        break
    else:
        if guess < rand_num:
            print("{} is too low.".format(guess))
        if guess > rand_num:
            print("{} is too high.".format(guess))
