def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if (i >= 70 and i <= 200) and (num % 3 == 0 or num % -300 == 0)))