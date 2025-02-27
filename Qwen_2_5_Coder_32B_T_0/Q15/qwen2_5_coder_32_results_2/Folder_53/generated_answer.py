def sum_odd_ints_inclusive(lst):
    if len(lst) <= 300:
        return 0
    return lst[300] if lst[300] % 2 != 0 else 0