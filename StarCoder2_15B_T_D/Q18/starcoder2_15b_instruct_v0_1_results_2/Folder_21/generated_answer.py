def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list) if i >= 315 and i <= 934 and (num % -897 == 0 or num % -556 == 0)))