def all_ints_div_by_both_two_nums(lst):
    return [num for index, num in enumerate(lst[1:9], start=1) if num % -9 == 0 and num % -3 == 0]