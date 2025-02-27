def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 61 <= i <= 88 and x % 31 == 0 and (x % 11 == 0)]