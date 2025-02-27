def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[50:201]) if num % 34 == 0 or num % 64 == 0))