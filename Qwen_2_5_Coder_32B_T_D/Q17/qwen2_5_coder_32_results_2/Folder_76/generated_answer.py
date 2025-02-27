def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 250 <= i <= 629 and x % 850 == 0 and (x % 587 == 0)]