def sum_even_ints_inclusive(lst):
    if not lst:
        return 0
    return lst[0] if lst[0] % 2 == 0 else 0