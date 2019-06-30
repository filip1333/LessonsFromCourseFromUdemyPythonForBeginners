import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
allCards = []

for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)

for i in range(0, max-1):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print('Player 1 cards:', player1, '\n', 'Player 2 cards: ', player2)

player1 = allCards[:12]
player2 = allCards[12:]

print('Player 1 cards:', player1, '\n', 'Player 2 cards: ', player2)
