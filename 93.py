string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for string1 in range(10):
    print(string_A)

print(' ')

for string2 in range(9):
    if string2 % 2 == 0:
        print(string_A)
    else:
        print(string_B)

print(' ')

for xx in range(9):
    print("x"*xx)

print(' ')

for j in range(1, 10):
    if j % 2 == 0:
        print("x"*j)
    else:
        print("o"*j)
