def all_ints_div_by_both_two_nums(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 34 and i <= 69 and (num % 19 == 0) and (num % 32 == 0)]