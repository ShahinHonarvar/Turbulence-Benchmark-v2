def all_ints_div_by_both_two_nums(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 11 and i <= 76 and (num % -81 == 0) and (num % -94 == 0)]