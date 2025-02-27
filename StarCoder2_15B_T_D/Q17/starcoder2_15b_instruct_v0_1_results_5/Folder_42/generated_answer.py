def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if i >= 29 and i <= 45 and (num % 27 == 0) and (num % 81 == 0)]