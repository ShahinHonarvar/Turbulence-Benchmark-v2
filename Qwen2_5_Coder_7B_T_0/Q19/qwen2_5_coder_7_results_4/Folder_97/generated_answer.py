def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 14 < i < 48 and x % 16 != 0]