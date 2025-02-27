def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 44 and i < 91 and (x % -68 != 0)]