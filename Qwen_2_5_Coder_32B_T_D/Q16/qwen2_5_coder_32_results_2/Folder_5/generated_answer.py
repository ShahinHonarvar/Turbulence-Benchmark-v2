def sum_even_ints_inclusive(lst):
    return lst[8] + lst[9] if 8 < len(lst) and 9 < len(lst) and (lst[8] % 2 == 0) and (lst[9] % 2 == 0) else 0