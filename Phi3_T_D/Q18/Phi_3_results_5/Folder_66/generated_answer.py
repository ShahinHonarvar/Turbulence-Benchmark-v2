def sum_ints_div_by_either_nums(lst):
    sum_divisible = sum((num for i, num in enumerate(lst[58:82]) if num % 55 == 0 or num % 10 == 0))
    return sum_divisible