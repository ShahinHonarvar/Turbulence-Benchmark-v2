def sum_even_ints_inclusive(lst):
    if len(lst) < 58:
        return 0
    return sum((x for x in lst[56:58] if x % 2 == 0))