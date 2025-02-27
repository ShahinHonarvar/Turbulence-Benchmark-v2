def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i in range(10) and x % 10 == 0 and (x % 100 == 0)]