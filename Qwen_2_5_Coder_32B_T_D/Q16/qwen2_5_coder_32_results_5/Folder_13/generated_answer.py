def sum_even_ints_inclusive(lst):
    if len(lst) < 88:
        return 0
    return sum((x for x in lst[25:88] if x % 2 == 0))