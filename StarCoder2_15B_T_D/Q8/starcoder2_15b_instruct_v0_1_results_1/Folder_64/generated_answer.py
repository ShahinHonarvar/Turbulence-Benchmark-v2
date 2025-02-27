def all_even_ints_exclusive(ints):
    even_ints = []
    for i in range(len(ints)):
        if i % 2 == 0 and 0 < i < 4:
            even_ints.append(ints[i])
    return even_ints