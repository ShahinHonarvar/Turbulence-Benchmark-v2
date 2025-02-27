def all_ints_not_div_by_num(lst):
    return [n for i, n in enumerate(lst) if i > 24 and i < 32 and (n % 35 != 0)]