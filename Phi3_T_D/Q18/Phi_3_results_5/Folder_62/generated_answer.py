def sum_ints_div_by_either_nums(int_list):
    start_index = 44
    end_index = 59
    return sum((x for x in int_list[start_index:end_index + 1] if x % 39 == 0 or x % 15 == 0)) or 0