def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 29 and i < 53 and (x % -68 != 0)]