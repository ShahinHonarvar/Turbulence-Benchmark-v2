def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 64 < i < 80 and x % -95 != 0]