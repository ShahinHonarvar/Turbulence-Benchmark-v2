def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 18 <= i <= 52 and x % 15 == 0 and (x % 57 == 0)]