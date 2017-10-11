coins = 0

print("You have {} coins.".format(coins))
answer = input("Do you want another? (yes/no) ")

while answer == "yes":
    coins += 1
    print("You have {} coins.".format(coins))
    answer = input("Do you want another? (yes/no) ")
print("Bye!")
