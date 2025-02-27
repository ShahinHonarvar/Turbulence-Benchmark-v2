def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 30 <= i <= 300 and x % 5 == 0]