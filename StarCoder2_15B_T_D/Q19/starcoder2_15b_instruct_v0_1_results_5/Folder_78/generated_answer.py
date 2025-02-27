def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 10 and i < 55 and (x % 36 != 0)]