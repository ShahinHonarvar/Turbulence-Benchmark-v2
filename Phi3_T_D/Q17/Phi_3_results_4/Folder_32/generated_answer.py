def all_ints_div_by_both_two_nums(int_list):
    divisible_list = [num for num in int_list[25:96] if num % 51 == 0 and num % 77 == 0]
    return divisible_list