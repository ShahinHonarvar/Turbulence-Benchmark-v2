def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 90 <= i <= 97 and x % 13 == 0 and (x % 35 == 0)]