def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 77 <= i <= 87 and x % 23 == 0 and (x % 57 == 0)]