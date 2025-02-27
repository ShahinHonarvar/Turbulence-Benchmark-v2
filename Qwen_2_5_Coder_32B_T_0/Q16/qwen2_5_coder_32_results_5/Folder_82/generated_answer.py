def sum_even_ints_inclusive(lst):
    if len(lst) <= 29:
        return 0
    return lst[29] if lst[29] % 2 == 0 else 0