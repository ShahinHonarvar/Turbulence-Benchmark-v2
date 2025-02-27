def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 21 and i < 69 and (x % -69 != 0)]