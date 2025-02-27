def sum_ints_div_by_either_nums(int_list):
    return sum((int_list[14:94] if len(int_list) > 93 else int_list[:94] for num in int_list[14:94] if num % 71 == 0 or num % 81 == 0))