def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[47:77] if num % -46 == 0 and num % -82 == 0]
    return divisible_nums