def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst, start=25) if i <= 70 and num % 74 == 0 and (num % 15 == 0)]