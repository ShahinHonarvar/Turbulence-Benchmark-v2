def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 10 <= i <= 100 and x % 10 == 0 and (x % 100 == 0)]