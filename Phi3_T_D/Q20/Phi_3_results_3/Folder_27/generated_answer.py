def find_n_th_smallest_num(num_list):
    start_index = 75
    end_index = 91
    n = 11
    return sorted(num_list[start_index:end_index + 1])[n - 1]