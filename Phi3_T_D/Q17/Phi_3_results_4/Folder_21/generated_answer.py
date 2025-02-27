def all_ints_div_by_both_two_nums(input_list):
    divisible_list = [num for num in input_list[315:935] if num % -897 == 0 and num % -556 == 0]
    return divisible_list