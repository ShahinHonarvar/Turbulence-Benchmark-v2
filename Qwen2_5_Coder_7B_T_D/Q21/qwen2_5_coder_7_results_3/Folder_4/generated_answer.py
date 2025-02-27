def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 12 and i <= 92 and (x % -14 == 0)]