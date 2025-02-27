def all_ints_not_div_by_num(int_list):
    ignore_num = -68
    return [num for num in int_list[45:91] if num % ignore_num != 0]