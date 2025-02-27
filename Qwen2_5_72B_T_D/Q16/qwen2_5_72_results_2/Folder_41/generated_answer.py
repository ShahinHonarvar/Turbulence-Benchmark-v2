def sum_even_ints_inclusive(lst):
    if 6 < len(lst):
        return lst[6] if lst[6] % 2 == 0 else 0
    return 0