def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i in range(8) and x % 2 == 0))