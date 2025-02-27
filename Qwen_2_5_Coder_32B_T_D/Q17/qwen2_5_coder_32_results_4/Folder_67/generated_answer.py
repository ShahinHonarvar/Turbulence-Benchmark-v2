def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 24 <= i <= 32 and x % 35 == 0 and (x % 87 == 0)]