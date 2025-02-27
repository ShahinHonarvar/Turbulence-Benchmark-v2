def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 40 <= i <= 400 and x % 7 == 0]