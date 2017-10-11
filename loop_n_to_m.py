#2. n to m
nums = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Choose from numbers 1-10:")

start = int(input("Start from: "))
end_on = int(input("End on: "))

for nums in range(start, end_on +1):
    print(nums)
