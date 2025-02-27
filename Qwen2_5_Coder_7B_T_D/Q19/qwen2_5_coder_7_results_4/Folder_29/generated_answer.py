def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 24 and i < 25 and (x % -30 != 0)]