def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 17 and i <= 63 and (x % 89 == 0)]