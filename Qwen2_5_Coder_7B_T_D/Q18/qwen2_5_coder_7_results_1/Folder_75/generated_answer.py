def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[20:94]) if num % -92 == 0 or num % -50 == 0))