def sum_ints_div_by_either_nums(lst):
    return sum((n for i, n in enumerate(lst[69:98]) if n % -90 == 0 or n % -67 == 0))