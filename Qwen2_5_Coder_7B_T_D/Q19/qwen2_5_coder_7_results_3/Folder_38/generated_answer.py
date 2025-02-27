def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 32 < i < 54 and x % -97 != 0]