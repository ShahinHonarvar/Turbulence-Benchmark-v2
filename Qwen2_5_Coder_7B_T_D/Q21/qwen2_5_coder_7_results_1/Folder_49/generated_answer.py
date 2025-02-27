def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 30 and i <= 300 and (x % 5 == 0)]