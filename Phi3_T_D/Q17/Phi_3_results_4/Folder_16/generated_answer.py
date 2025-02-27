def all_ints_div_by_both_two_nums(int_list):
    start_index, end_index = (55, 80)
    divisible_ints = [num for num in int_list[start_index:end_index + 1] if num % 22 == 0 and num % 32 == 0]
    return divisible_ints