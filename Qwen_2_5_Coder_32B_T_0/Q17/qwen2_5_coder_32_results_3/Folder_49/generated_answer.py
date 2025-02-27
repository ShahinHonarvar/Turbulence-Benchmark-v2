def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 80 <= i <= 200 and x % 10 == 0 and (x % 1000 == 0)]