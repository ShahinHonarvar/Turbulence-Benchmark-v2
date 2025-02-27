def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 1 and i <= 4 and (x % -6 == 0)]