def all_ints_div_by_both_two_nums(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 13 and i <= 18 and (num % 45 == 0) and (num % 20 == 0)]