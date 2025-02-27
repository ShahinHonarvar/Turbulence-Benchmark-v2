def sum_even_ints_inclusive(ints):
    even_ints = [i for i in ints if i % 2 == 0]
    if len(even_ints) > 66:
        return sum(even_ints[10:67])
    else:
        return 0