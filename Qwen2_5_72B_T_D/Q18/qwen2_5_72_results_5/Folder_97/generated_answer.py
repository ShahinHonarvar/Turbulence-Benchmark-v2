def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[58:76]) if num % 72 == 0 or num % 62 == 0))