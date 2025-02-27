def sum_odd_ints_inclusive(lst):
    if 300 <= len(lst):
        return lst[300] if lst[300] % 2 != 0 else 0
    return 0