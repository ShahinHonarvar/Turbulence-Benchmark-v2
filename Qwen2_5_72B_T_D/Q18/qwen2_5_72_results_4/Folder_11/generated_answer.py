def sum_ints_div_by_either_nums(lst):
    relevant_nums = lst[22:25]
    return sum((num for num in relevant_nums if num % -85 == 0 or num % -30 == 0))