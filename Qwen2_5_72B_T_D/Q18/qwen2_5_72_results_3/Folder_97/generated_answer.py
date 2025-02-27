def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 58 <= i <= 75 and (num % 72 == 0 or num % 62 == 0)))