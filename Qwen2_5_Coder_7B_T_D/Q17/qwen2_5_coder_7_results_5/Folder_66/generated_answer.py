def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 58 and i <= 81 and (num % 55 == 0) and (num % 10 == 0)]