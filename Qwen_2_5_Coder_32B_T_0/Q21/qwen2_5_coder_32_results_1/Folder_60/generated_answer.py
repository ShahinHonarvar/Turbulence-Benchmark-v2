def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 31 <= i <= 67 and x % -15 == 0]