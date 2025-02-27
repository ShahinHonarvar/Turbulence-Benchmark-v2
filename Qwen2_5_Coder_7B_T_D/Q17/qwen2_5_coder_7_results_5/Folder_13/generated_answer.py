def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 13 and i <= 18 and (x % 45 == 0) and (x % 20 == 0)]