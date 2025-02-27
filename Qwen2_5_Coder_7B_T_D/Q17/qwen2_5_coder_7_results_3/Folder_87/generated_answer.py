def all_ints_div_by_both_two_nums(lst):
    return [n for i, n in enumerate(lst) if 18 <= i <= 52 and n % 15 == 0 and (n % 57 == 0)]