def all_ints_div_by_both_two_nums(int_list):
    divisor_1 = -46
    divisor_2 = -82
    return [num for num in int_list[48:77] if num % divisor_1 == 0 and num % divisor_2 == 0]