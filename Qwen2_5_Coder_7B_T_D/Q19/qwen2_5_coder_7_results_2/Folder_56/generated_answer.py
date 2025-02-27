def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 7 < i < 9 and x % -9 != 0]