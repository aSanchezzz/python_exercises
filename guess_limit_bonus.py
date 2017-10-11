replay = "y"
def guessGame():

    import random

    rand_num = random.randint(1, 10)
    guess_tried = 0

    print("I am thinking of a number between 1 and 10")
    while True:
        guess = int(input("What's the number? "))
        if guess == rand_num:
            print("Yes, you win!")
            break
        else:
            if guess < rand_num:
                print("{} is too low.".format(guess))
                break
            if guess > rand_num:
                print("{} is too high.".format(guess))
                guess_tried +=1
            guess_left = 5 - guess_tried
            print("You have {} guesses left.".format(guess_left))
            if guess_tried == 5:
                print('You ran out of guesses!')
                global replay
                replay = input("Do you want to play again? ")
                break
while True:
    if replay == "y":
        guessGame()
    elif replay == "n":
        print("See you next time!")
        break
