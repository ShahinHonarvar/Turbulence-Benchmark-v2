def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if (i >= 7 and i <= 7) and (num % 5 == 0 or num % 7 == 0)))