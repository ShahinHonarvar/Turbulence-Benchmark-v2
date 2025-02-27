def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 0 < i < 3 and x % -2 != 0]