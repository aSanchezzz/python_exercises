bill = float(input("Total bill amount: "))

serviceQuality = str(input("The level of service (good, fair, or bad): "))

if serviceQuality == 'good':
    tip = .20
if  serviceQuality == 'fair':
    tip = .15
if serviceQuality == 'bad':
    tip = .10

totalBill = (bill * tip) + bill;

print("Tip amount", (tip * 100))
print("Total amount: ", totalBill)
