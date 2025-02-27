def all_ints_div_by_num(int_list):
    start_index = 574
    end_index = 744
    return [x for x in int_list[start_index:end_index + 1] if x % 649 == 0]