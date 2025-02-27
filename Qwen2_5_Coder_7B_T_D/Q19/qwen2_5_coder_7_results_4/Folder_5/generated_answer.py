def all_ints_not_div_by_num(lst):
    return [n for i, n in enumerate(lst) if 1 < i < 3 and n % 8 != 0]