def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 16 < i < 87 and x % -15 != 0]