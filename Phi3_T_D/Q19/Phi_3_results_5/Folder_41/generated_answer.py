def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list[0:9]) if num % -3 != 0]