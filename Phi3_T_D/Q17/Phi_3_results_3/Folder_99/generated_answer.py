def all_ints_div_by_both_two_nums(integer_list):
    divisible_ints = [num for num in integer_list[154:799] if num % 275 == 0 and num % 580 == 0]
    return divisible_ints