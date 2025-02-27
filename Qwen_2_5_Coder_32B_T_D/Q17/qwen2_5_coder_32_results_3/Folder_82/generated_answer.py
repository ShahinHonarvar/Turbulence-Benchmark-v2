def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 20 <= i <= 200 and x % -20 == 0 and (x % -200 == 0)]