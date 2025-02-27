def all_ints_div_by_both_two_nums(lst):
    return [num for idx, num in enumerate(lst[10:29], start=10) if num % -61 == 0 and num % -64 == 0]