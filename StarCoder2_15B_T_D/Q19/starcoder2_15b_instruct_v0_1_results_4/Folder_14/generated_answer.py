def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 2 and i < 7 and (x % 8 != 0)]