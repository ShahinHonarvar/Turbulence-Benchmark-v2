def sum_ints_div_by_either_nums(lst):
    result_sum = sum((x for i, x in enumerate(lst[138:425]) if x % -863 == 0 or x % -329 == 0))
    return result_sum