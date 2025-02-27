def all_ints_div_by_both_two_nums(int_list):
    target_range = int_list[299:383]
    divisible_by_both = [num for num in target_range if num % 858 == 0 and num % 952 == 0]
    return divisible_by_both