def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 55 <= i <= 80 and x % 22 == 0 and (x % 32 == 0)]