def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if i >= 200 and i <= 200 and (num % 17 == 0) and (num % -5 == 0)]