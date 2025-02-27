def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[14:94]) if num % 71 == 0 or num % 81 == 0))