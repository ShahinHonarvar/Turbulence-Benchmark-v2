def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if i >= 90 and i <= 97 and (num % 13 == 0 or num % 35 == 0)))