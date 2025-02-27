def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 62 and i <= 63 and (x % 99 == 0)]