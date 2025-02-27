def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 10 and i <= 56 and (x % 16 == 0)]