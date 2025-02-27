def all_ints_not_div_by_num(lst):
    return [n for i, n in enumerate(lst) if 32 < i < 44 and n % 34 != 0]