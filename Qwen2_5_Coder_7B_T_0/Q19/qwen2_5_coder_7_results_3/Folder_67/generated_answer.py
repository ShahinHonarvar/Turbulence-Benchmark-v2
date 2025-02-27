def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 48 < i < 92 and x % 90 != 0]