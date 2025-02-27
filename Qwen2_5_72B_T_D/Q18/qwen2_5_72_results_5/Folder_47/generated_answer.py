def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[42:88]) if num % -90 == 0 or num % -74 == 0))