def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[42:44] if num % 15 == 0 or num % 87 == 0))