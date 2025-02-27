def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 31 and i <= 72 and (x % -63 == 0)]