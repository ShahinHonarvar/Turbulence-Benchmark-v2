def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 59 and i <= 79 and (num % -82 == 0)]