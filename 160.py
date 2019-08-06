def give_geom_seq_element(a1=2, factor=2, index=2):
    # returns n-th term of geometric sequence starting with element a1
    value = a1 * pow(factor, index - 1)
    return value


print(print('2^64 =', give_geom_seq_element(1, 2, 64)))

a1 = 3
factor = 2
maxIndex = 10

for i in range(1, maxIndex):
    n = (give_geom_seq_element(a1=a1, factor=factor, index=i))
    print('Term ', i, '=', n)


def give_factor_for_geom_seq(term, nextterm):
    # returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term


print(give_factor_for_geom_seq(12, 24))
