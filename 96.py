i = 10
result = 1

for j in range(1, i+1):
    result *= j

print(i, result)

print(' ')

x = 10

for k in range(1, x+1):
    r = 1
    for m in range(1, i+1):
        r *= m

    print(k, r)

print(' ')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for n in list_noun:
    for a in list_adj:
        print(n, a)
