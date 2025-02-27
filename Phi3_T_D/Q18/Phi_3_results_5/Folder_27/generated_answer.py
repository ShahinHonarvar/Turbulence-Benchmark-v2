def sum_ints_div_by_either_nums(lst):
    return sum((n for n in lst[20:36] if n % -36 == 0 or n % -89 == 0))