min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 55

if num_likes >= min_likes and num_shares >= min_shares:
    print('We have it! Now there will be a 10% reduction on our products')
else:
    print('The goal could not be achieved')

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if (isBigDrinkOrdered and isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
else:
    print('Come to us on weekend and consider buying Pizza or BigDrink to have Burger for free')

diskSize = 140
diskSizeUsed = 133
fileSize = 10

if fileSize <= (diskSize - diskSizeUsed):
    print("File can be downloaded")
else:
    print("You do not have disk space")
