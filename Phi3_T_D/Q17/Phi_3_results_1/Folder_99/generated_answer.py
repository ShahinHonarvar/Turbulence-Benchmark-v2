def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = [num for num in int_list[154:799] if num % 275 == 0 and num % 580 == 0]
    return divisible_by_both