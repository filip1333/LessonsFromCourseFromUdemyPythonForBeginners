import random

for i in range(10):
    print(random.randint(1, 100))

print(' ')

number1 = random.randint(1, 100)
print(number1)
counter = 1
number2 = random.randint(1, 100)
while True:
    if number2 != number1:
        counter += 1
        number2 = random.randint(1, 100)
        print(counter, number2)
    else:
        print("It needed %d attempts to generate %d again" % (counter, number1))
        break

print(' ')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
]

random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print('"----Group %d ----"' % (groupNumber))
    print(countries[i])
