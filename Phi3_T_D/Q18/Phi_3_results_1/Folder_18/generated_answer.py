def sum_ints_div_by_either_nums(lst):
    result = sum((val for idx, val in enumerate(lst[55:67]) if val % 22 == 0 or val % 82 == 0))
    return result