def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[56:89]) if num % -59 == 0 or num % -79 == 0))