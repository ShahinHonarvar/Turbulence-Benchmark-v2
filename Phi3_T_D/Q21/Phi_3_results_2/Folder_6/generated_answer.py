def all_ints_div_by_num(int_list):
    start_index = 13
    end_index = 63
    result = [num for num in int_list[start_index:end_index + 1] if num % 46 == 0]
    return result