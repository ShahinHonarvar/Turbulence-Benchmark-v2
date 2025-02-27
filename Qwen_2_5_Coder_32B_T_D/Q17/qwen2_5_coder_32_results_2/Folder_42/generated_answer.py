def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 29 <= i <= 45 and x % 27 == 0 and (x % 81 == 0)]