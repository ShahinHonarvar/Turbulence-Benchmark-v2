def sum_even_ints_inclusive(lst):
    if len(lst) < 89:
        return 0
    return sum((x for x in lst[22:89] if x % 2 == 0))