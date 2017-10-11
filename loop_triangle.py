# height = int(input("Triangle height: "))

xr = 5

for x in range(0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print(' ' * spaces + '*' * stars)
