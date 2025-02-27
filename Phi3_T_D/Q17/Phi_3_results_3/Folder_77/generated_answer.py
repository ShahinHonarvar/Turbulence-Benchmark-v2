def all_ints_div_by_both_two_nums(int_list):
    divisor = 649 * 461
    return [num for num in int_list[828:933] if num % divisor == 0]