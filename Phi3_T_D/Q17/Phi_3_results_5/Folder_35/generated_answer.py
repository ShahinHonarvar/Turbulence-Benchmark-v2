def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [num for num in int_list[77:88] if num % 23 == 0 and num % 57 == 0]
    return divisible_ints