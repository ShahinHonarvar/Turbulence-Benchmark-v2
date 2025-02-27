def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 1 and i <= 8 and (num % -9 == 0) and (num % -3 == 0)]