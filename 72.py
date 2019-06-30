min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 55

if num_likes >= min_likes and num_shares >= min_shares:
    print("We start the promotion!")
elif num_likes < min_likes and num_shares >= min_shares:
    print("It's not enough likes to promotion")
elif num_likes >= min_likes and num_shares < min_shares:
    print("It's not enought shares to promotion")


orderPizza = True
bigDrink = True
isWeekend = True

if orderPizza and bigDrink and isWeekend is True:
    print('You get a burger promotion')
elif orderPizza is not True:
    print('You must order pizza to get a burger promotion')
elif bigDrink is not True:
    print('You must order big drink to get a burger promotion')
elif isWeekend is not True:
    print('The burger promotion is only on the weekend')

