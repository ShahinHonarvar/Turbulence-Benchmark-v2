def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 34 <= i <= 69 and x % 19 == 0 and (x % 32 == 0)]