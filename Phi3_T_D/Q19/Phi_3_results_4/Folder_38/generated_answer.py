def all_ints_not_div_by_num(int_list):
    range_list = int_list[32:54]
    filtered_list = [num for num in range_list if num % -97 != 0]
    return filtered_list