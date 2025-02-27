def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 54 and i <= 79 and (num % 54 == 0) and (num % 28 == 0)]