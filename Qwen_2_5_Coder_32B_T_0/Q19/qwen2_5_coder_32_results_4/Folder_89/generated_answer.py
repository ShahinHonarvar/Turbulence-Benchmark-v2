def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 48 < i < 62 and x % 28 != 0]