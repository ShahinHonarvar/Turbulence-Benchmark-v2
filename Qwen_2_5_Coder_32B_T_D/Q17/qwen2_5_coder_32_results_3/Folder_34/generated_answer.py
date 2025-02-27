def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 60 <= i <= 200 and x % 9 == 0 and (x % 11 == 0)]