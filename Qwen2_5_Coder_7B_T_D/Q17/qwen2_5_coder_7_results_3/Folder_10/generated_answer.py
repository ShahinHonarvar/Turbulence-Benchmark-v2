def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst[32:100]) if num % -11 == 0 and num % -15 == 0]