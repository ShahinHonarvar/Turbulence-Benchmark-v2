def all_ints_div_by_num(int_list):
    start_index = 8
    end_index = 8
    return [num for num in int_list[start_index:end_index + 1] if num % -7 == 0]