def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 24 <= i <= 32 and (num % 35 == 0 or num % 87 == 0)))