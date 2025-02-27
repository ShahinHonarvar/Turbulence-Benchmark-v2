def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = [num for num in int_list[48:60] if num % 88 == 0 and num % 58 == 0]
    return divisible_by_both