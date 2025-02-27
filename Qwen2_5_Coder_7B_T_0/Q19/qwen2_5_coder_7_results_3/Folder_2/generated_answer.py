def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 20 < i < 50 and x % 40 != 0]