def all_ints_div_by_both_two_nums(lst):
    return [n for i, n in enumerate(lst) if i >= 90 and i <= 200 and (n % 31 == 0) and (n % 13 == 0)]