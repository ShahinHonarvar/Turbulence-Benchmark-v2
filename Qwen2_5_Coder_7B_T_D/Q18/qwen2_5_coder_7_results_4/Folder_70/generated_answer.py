def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[42:44]) if num % 15 == 0 or num % 87 == 0))