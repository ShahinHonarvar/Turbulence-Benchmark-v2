def all_ints_not_div_by_num(int_list):
    filtered_ints = [num for num in int_list[51:81] if num % 64 != 0]
    return filtered_ints