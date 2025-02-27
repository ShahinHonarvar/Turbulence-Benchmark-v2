def all_ints_div_by_num(int_list):
    start_index = 66
    end_index = 81
    return [num for num in int_list[start_index:end_index + 1] if num % 77 == 0]