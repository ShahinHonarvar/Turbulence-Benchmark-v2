def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 11 <= i <= 46 and (num % 55 == 0 or num % 36 == 0)))