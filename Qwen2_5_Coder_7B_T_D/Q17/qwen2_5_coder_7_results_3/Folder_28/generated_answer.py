def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 34 and i <= 81 and (x % 27 == 0) and (x % 57 == 0)]