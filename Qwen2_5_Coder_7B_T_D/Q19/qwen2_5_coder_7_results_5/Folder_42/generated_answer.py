def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 11 and i < 56 and (x % 90 != 0)]