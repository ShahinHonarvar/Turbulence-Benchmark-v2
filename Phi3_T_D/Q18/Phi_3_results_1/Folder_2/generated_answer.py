def sum_ints_div_by_either_nums(lst):
    total_sum = sum((n for n in lst[73:87] if n % 54 == 0 or n % 82 == 0))
    return total_sum