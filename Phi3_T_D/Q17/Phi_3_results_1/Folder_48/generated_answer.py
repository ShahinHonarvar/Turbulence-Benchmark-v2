def all_ints_div_by_both_two_nums(int_list):
    divisible_list = [num for num in int_list[306:958] if num % 982 == 0 and num % 319 == 0]
    return divisible_list