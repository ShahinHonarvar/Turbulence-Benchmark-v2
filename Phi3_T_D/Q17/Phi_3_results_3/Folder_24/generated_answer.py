def all_ints_div_by_both_two_nums(lst):
    divisor1 = -68
    divisor2 = -85
    target_range = range(29, 54)
    return [num for num in lst[target_range] if num % divisor1 == 0 and num % divisor2 == 0]