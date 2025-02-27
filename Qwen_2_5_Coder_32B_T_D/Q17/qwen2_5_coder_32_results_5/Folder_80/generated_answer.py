def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 14 <= i <= 93 and x % 71 == 0 and (x % 81 == 0)]