def sum_ints_div_by_either_nums(lst):
    return sum((n for i, n in enumerate(lst[86:90]) if n % -61 == 0 or n % -79 == 0))