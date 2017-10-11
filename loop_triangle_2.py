height = int(input("Height: "))

for x in range(0,height):
    spaces = height - x - 1
    stars = x * 2 + 1
    print(' ' * spaces + '*' * stars)
