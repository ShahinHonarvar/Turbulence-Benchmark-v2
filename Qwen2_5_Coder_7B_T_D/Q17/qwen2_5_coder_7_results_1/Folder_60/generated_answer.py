def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 10 and i <= 79 and (x % -74 == 0) and (x % -58 == 0)]