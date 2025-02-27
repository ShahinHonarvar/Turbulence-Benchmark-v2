def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [num for num in int_list[81:87] if num % -33 == 0 and num % -62 == 0]
    return divisible_ints