def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 35 <= i <= 64 and x % -30 == 0 and (x % -95 == 0)]