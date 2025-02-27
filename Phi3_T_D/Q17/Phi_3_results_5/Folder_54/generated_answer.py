def all_ints_div_by_both_two_nums(num_list):
    divisible_nums = [num for num in num_list[13:92] if num % -65 == 0 and num % -62 == 0]
    return divisible_nums