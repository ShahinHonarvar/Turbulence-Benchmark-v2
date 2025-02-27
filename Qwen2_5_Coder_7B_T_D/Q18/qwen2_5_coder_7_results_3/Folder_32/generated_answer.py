def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 25 <= i <= 95 and (num % 51 == 0 or num % 77 == 0)))