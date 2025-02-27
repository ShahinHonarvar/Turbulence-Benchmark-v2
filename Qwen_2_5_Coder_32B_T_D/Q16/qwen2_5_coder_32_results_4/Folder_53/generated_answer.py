def sum_even_ints_inclusive(lst):
    if len(lst) < 112:
        return 0
    return lst[111] if lst[111] % 2 == 0 else 0