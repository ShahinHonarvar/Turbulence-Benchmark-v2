def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 28 and i <= 96 and (x % 90 == 0) and (x % 97 == 0)]