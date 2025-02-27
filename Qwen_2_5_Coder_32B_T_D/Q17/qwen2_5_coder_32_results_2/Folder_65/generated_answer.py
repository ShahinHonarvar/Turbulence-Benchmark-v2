def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 50 <= i <= 92 and x % -94 == 0 and (x % -95 == 0)]