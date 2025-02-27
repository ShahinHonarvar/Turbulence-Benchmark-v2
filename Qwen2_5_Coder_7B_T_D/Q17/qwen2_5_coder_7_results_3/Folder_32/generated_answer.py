def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 95 and (x % 51 == 0) and (x % 77 == 0)]