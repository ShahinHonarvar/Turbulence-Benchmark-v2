def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[13:19]) if num % 45 == 0 or num % 20 == 0))