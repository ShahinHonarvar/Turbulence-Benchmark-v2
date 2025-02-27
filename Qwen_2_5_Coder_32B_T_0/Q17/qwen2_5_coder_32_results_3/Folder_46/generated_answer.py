def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 11 <= i <= 46 and x % 55 == 0 and (x % 36 == 0)]