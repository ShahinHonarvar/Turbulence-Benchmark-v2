def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 1 <= i <= 4 and x % -6 == 0]