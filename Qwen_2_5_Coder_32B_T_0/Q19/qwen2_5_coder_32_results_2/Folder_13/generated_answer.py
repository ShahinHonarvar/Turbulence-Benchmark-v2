def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 32 < i < 44 and x % 34 != 0]