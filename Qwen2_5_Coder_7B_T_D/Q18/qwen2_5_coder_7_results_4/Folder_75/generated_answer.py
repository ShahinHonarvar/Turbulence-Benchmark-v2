def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if i >= 20 and i <= 93 and (num % -92 == 0 or num % -50 == 0)))