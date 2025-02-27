def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 13 and i < 70 and (x % -78 != 0)]