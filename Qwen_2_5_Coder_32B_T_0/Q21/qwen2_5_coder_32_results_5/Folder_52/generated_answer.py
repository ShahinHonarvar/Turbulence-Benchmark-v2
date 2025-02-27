def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 42 <= i <= 97 and x % 46 == 0]