def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 27 <= i <= 86 and x % 29 == 0]