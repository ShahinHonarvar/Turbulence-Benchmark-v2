def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 54 and i <= 79 and (x % 54 == 0) and (x % 28 == 0)]