def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 72 and i <= 93 and (x % 32 == 0) and (x % 44 == 0)]