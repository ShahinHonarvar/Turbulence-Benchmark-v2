def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if (i >= 81 and i <= 89) and (num % 56 == 0 or num % 68 == 0)))