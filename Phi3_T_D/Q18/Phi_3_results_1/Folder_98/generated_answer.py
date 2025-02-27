def sum_ints_div_by_either_nums(lst):
    total_sum = sum((val for i, val in enumerate(lst[0:6]) if val % 13 == 0 or val % -1 == 0))
    return total_sum