import random

min = 1
max = 6
dice = random.randint(min, max)
print(dice)

if dice == 1:
    print('   \n o \n   ')
elif dice == 2:
    print('  o\n   \no  ')
elif dice == 3:
    print('  o\n o \no  ')
elif dice == 4:
    print('o o\n   \no o')
elif dice == 5:
    print('o o\n o \no o')
else:
    print('o o\no o\no o')

print(' ')

dices = []
for i in range(5):
    dices.append(random.randint(min, max))

dices.sort()
print(dices)
