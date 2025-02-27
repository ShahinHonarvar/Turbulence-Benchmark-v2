def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 42 and i <= 87 and (x % 90 == 0) and (x % 74 == 0)]