def all_even_ints_exclusive(ints):
    even_ints = []
    for i, val in enumerate(ints):
        if i >= 111 and i < 473 and (val % 2 == 0):
            even_ints.append(val)
    return even_ints