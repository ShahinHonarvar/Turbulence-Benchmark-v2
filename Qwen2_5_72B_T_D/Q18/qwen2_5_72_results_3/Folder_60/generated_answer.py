def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[10:80], start=10) if i >= 10 and (num % -74 == 0 or num % -58 == 0)))