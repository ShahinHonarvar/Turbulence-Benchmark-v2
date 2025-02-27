def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 18 and i <= 38 and (x % -97 == 0)]