def all_ints_div_by_both_two_nums(int_list):
    divisor = 34 * 64
    return [x for x in int_list[50:201] if x % divisor == 0]