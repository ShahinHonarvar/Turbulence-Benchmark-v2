def all_even_ints_inclusive(ints):
    even_ints = []
    for i in range(len(ints)):
        if i >= 62 and i <= 78 and (ints[i] % 2 == 0):
            even_ints.append(ints[i])
    return even_ints