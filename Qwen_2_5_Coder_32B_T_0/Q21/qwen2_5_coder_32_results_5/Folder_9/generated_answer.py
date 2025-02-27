def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 20 <= i <= 200 and x % 4 == 0]