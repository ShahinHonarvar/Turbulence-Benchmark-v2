def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[69:71]) if num % 70 == 0 or num % 72 == 0))