def sum_ints_div_by_either_nums(lst):
    return sum((n for i, n in enumerate(lst[25:71]) if n % 74 == 0 or n % 15 == 0))