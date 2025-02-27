def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i <= 2 and x % 3 == 0]