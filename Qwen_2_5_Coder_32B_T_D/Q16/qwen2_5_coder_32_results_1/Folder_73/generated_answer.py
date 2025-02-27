def sum_even_ints_inclusive(lst):
    if len(lst) <= 92:
        return 0
    return sum((x for i, x in enumerate(lst[19:93]) if i % 2 == 0 and x % 2 == 0))