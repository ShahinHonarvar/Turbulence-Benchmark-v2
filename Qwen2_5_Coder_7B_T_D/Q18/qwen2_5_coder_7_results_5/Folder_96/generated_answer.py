def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst, start=50) if 200 >= i >= 50 and (num % -34 == 0 or num % 64 == 0)))