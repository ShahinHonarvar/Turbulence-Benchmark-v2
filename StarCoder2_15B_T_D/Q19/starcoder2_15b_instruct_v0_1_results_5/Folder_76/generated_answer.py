def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 361 and i < 887 and (x % 877 != 0)]