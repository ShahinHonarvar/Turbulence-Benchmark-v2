def sum_ints_div_by_either_nums(lst):
    return sum((n for i, n in enumerate(lst) if 20 <= i <= 200 and (n % -20 == 0 or n % -200 == 0)))