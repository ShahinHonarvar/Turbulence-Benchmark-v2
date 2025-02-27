def sum_odd_ints_inclusive(ints):
    return sum((x for i, x in enumerate(ints) if i >= 30 and i <= 200 and (x % 2 != 0)))