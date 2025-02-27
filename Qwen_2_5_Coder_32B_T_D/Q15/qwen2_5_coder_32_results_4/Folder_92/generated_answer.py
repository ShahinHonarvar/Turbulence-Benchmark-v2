def sum_odd_ints_inclusive(lst):
    return lst[1] if 1 < len(lst) and lst[1] % 2 != 0 else 0