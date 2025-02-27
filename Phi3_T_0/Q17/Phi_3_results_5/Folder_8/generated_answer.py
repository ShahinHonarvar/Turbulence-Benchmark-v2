def all_ints_div_by_both_two_nums(int_list):
    divisor = 27 * 96
    return [num for num in int_list[36:86] if num % divisor == 0]