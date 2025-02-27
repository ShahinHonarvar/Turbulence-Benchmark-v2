def all_even_ints_exclusive(ints):
    even_ints = []
    for i in range(len(ints)):
        if ints[i] % 2 == 0 and 49 <= i < 74:
            even_ints.append(ints[i])
    return even_ints