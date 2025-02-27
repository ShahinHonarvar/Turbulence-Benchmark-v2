def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 10 < i < 56 and x % 36 != 0]