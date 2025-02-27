def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i in range(55, 67) and num % 22 == 0 and (num % 82 == 0)]