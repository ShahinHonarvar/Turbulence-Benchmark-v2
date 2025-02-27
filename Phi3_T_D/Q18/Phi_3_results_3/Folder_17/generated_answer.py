def sum_ints_div_by_either_nums(lst):
    sum_divisible = sum((val for val in lst[81:90] if val % 56 == 0 or val % 68 == 0))
    return sum_divisible