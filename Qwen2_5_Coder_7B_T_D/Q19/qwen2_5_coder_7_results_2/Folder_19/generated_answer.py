def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 4 < i < 6 and x % -7 != 0]