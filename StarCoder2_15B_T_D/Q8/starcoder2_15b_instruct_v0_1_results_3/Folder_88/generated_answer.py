def all_even_ints_exclusive(ints):
    even_ints = []
    for i in range(2, 8):
        if ints[i] % 2 == 0:
            even_ints.append(ints[i])
    return even_ints