def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 10 and i < 100 and (x % 100 != 0)]