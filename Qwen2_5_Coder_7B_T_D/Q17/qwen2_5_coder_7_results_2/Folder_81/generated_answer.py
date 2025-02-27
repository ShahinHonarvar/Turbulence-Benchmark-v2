def all_ints_div_by_both_two_nums(lst):
    return [n for i, n in enumerate(lst, 1) if i >= 10 and i <= 100 and (n % 10 == 0) and (n % 100 == 0)]