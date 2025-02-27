def all_ints_div_by_both_two_nums(int_list):
    divisible_list = [num for i, num in enumerate(int_list) if num % 54 == 0 and num % 28 == 0 and (54 <= i <= 79)]
    return divisible_list