def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 80 and (x % 20 == 0) and (x % 26 == 0)]