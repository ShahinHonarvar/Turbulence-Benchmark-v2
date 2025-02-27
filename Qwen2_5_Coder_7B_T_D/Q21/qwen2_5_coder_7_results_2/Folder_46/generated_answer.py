def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 21 and i <= 97 and (x % 46 == 0)]