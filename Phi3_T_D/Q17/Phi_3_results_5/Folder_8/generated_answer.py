def all_ints_div_by_both_two_nums(int_list):
    both_divisible = [num for num in int_list[35:86] if num % -27 == 0 and num % -96 == 0]
    return both_divisible