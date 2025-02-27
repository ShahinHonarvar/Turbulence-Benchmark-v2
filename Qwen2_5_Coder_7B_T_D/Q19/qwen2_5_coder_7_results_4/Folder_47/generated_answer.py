def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 25 and i < 76 and (x % -53 != 0)]