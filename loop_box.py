width = int(input("Width: "))
height = int(input("Height: "))
num_spaces = width - 2

#create top row
print("*" * width)

#create center
spaces = ' ' * num_spaces
for i in range(1, height - 1):
    print("*" + spaces + "*")
#create top
print("*" * width)
