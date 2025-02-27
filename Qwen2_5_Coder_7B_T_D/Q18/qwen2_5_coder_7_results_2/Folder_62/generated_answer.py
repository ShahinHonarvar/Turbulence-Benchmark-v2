def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[44:60]) if num % 39 == 0 or num % 15 == 0))