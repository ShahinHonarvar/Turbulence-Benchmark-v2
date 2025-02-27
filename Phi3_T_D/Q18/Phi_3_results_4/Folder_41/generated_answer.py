def sum_ints_div_by_either_nums(int_list):
    return sum((num for idx, num in enumerate(int_list[:10]) if num % 6 == 0 or num % -3 == 0))