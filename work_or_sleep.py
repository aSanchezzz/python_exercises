day = int(input('Day (0-6)? '))

while True:
    if day == 0 or 6:
        print("Sleep in")
        break
    else:
        print("Work")
