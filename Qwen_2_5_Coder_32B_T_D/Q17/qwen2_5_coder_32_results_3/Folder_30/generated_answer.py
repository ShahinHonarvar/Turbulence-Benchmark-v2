def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 11 <= i <= 76 and x % -81 == 0 and (x % -94 == 0)]