def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 6 and i <= 8 and (x % -9 == 0)]