def sum_ints_div_by_either_nums(lst):
    total_sum = sum((val for idx, val in enumerate(lst[55:81], start=55) if val % 22 == 0 or val % 32 == 0))
    return total_sum