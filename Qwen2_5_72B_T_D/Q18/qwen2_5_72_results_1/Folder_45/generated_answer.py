def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[30:201]) if num % 115 == 0))