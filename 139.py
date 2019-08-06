import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace',  'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10',   'Power': 10},
    {'Figure': '9',    'Power': 9}]

max = len(figures)
print(max)

for i in range (0, max-1):
    allCards = []
    for c in colors:
        for f in figures:
            aCard = f.copy()
            aCard['Color'] = c
            allCards.append(aCard)

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print('Player 1 cards:', player1, '\n', 'Player 2 cards: ', player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    shadowCard = []
    stack = []

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print('Cards are equal. Player 1 card: ', card1, ' Player 2 card: ', card2, ' it\'s war time')
        while card1["Power"] == card2["Power"]:
            shadowCard.append(card1)
            shadowCard.append(card2)
            if len(player1) < 2:
                player2.extend(shadowCard)
                player2.extend(player1)
                player1 = []
                print('Player 2 have all cards')
                break
            elif len(player2) < 2:
                player1.extend(shadowCard)
                player1.extend(player1)
                player2 = []
                print('Player 1 have all cards')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                shadowCard.append(card1)
                shadowCard.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('Player 1 card ', card1, ' is stronger that Player 2 card ', card2,
                      ' Player 1 has', len(player1), ' cards, Player 2 has ', len(player2), ' cards')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('Player 2 card ', card2, ' is stronger that Player 1 card ', card1,
                      ' Player 1 has', len(player1), ' cards, Player 2 has ', len(player2), ' cards')

    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('Player 1 card ', card1, ' is stronger that Player 2 card ', card2,
              ' Player 1 has', len(player1), ' cards, Player 2 has ', len(player2), ' cards')
    else:
        player2.append(card1)
        player2.append(card2)
        print('Player 2 card ', card2, ' is stronger that Player 1 card ', card1,
              ' Player 1 has', len(player1), ' cards, Player 2 has ', len(player2), ' cards')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')