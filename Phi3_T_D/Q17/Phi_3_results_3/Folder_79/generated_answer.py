def all_ints_div_by_both_two_nums(int_list):
    target_range = int_list[8:10]
    divisible_by_both = [num for num in target_range if num % -3 == 0 and num % 6 == 0]
    return divisible_by_both