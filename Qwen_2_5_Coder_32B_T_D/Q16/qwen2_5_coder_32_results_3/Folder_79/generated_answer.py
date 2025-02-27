def sum_even_ints_inclusive(lst):
    if 4 < len(lst) - 1:
        return lst[4] if lst[4] % 2 == 0 else 0
    return 0