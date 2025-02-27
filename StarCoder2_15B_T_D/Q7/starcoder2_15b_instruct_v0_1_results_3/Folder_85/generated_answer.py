def all_even_ints_inclusive(ints):
    evens = []
    for i in range(6, 9):
        if ints[i] % 2 == 0:
            evens.append(ints[i])
    return evens