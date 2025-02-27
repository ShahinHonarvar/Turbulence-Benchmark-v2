def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 14 and i <= 68 and (x % 18 == 0)]