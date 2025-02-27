def all_even_ints_exclusive(values):
    even_ints = []
    for i, value in enumerate(values):
        if i >= 13 and i < 70 and (value % 2 == 0):
            even_ints.append(value)
    return even_ints