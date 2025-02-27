def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 78 <= i <= 81 and x % 76 == 0 and (x % 60 == 0)]