def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 77 and i <= 87 and (num % 23 == 0) and (num % 57 == 0)]