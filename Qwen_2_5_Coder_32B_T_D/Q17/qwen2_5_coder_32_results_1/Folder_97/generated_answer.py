def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 58 and i <= 75 and (x % 72 == 0) and (x % 62 == 0)]