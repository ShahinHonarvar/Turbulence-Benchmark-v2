def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 17 < i < 88 and x % -75 != 0]