def find_n_th_smallest_num(num_list):
    if not 11 <= len(num_list) <= 24:
        raise ValueError('List must contain between 11 and 24 elements.')
    return sorted(num_list[10:25])[9]