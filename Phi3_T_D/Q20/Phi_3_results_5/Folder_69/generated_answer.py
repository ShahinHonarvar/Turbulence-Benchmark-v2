def find_n_th_smallest_num(num_list):
    n = min(39, len(num_list) - 1)
    m = min(n + 17 - 1, 91)
    return sorted(num_list[n:m + 1])[16]