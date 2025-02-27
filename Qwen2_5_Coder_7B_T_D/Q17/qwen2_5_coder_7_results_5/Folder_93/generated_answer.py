def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 86 and i <= 89 and (x % 61 == 0) and (x % 79 == 0)]