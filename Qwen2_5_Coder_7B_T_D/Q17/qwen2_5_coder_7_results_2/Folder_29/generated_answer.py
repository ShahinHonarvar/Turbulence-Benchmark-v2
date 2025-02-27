def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i in range(55, 85) and num % 24 == 0 and (num % 11 == 0)]