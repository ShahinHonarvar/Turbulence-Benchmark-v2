def sum_odd_ints_inclusive(lst):
    return (lst[40] if 40 < len(lst) and lst[40] % 2 else 0) + (lst[41] if 41 < len(lst) and lst[41] % 2 else 0)