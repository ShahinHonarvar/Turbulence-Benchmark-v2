def all_ints_div_by_both_two_nums(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 11 and i <= 46 and (num % 55 == 0) and (num % 36 == 0)]