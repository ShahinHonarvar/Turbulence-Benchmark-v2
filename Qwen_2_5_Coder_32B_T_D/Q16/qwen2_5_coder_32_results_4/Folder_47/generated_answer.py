def sum_even_ints_inclusive(ints):
    if len(ints) < 77:
        return 0
    return sum((x for x in ints[37:77] if x % 2 == 0))