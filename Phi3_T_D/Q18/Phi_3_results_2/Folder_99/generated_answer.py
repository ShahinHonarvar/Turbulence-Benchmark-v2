def sum_ints_div_by_either_nums(int_list):
    start_index = 154
    end_index = 798
    total_sum = sum((i for i in int_list[start_index:end_index + 1] if i % 275 == 0 or i % 580 == 0))
    return total_sum