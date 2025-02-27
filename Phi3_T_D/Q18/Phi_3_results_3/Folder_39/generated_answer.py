def sum_ints_div_by_either_nums(lst):
    total_sum = sum((val for idx, val in enumerate(lst[13:77], start=13) if val % -66 == 0 or val % -32 == 0))
    return total_sum