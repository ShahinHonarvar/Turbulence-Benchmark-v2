def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 61 <= i <= 88 and num % 31 == 0 and (num % 11 == 0)]