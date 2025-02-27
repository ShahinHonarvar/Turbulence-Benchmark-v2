def all_ints_div_by_both_two_nums(int_list):
    divisor = 34 * 64
    return [num for num in int_list[50:201] if num % divisor == 0]