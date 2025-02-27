def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 25 <= i <= 95 and x % 51 == 0 and (x % 77 == 0)]