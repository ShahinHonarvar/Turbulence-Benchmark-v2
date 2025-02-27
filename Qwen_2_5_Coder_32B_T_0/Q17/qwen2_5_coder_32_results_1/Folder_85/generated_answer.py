def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 1 <= i <= 8 and x % -9 == 0 and (x % -3 == 0)]