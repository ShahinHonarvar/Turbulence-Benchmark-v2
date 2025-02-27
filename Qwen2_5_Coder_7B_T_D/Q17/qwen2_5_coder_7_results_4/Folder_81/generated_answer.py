def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 10 and i <= 100 and (num % 10 == 0) and (num % 100 == 0)]