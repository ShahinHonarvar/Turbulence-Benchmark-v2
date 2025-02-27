def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 4 and i < 7 and (x % -6 != 0)]