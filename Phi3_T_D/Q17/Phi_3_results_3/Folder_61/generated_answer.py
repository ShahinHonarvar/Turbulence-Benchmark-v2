def all_ints_div_by_both_two_nums(int_list):
    divisible_range = int_list[0:7]
    return [num for num in divisible_range if num % -5 == 0 and num % -6 == 0]