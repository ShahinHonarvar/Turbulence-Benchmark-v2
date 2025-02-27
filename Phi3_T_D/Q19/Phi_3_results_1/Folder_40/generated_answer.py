def all_ints_not_div_by_num(int_list):
    return [num for index, num in enumerate(int_list[1:3]) if num % 1 != 0]