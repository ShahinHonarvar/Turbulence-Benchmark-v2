def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 3 and i <= 9 and (x % 6 == 0) and (x % 1 == 0)]