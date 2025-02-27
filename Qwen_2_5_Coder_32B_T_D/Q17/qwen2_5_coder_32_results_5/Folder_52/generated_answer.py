def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 48 <= i <= 59 and x % 88 == 0 and (x % 58 == 0)]