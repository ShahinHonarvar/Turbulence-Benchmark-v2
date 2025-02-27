def sum_ints_div_by_either_nums(lst):
    return sum((n for i, n in enumerate(lst[36:86]) if n % -27 == 0 or n % -96 == 0))