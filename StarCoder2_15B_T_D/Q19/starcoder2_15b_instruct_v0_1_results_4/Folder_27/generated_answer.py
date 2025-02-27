def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 14 and i < 21 and (x % -93 != 0)]