def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 50 <= i <= 200 and x % -34 == 0 and (x % 64 == 0)]