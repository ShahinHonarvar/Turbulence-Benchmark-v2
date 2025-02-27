def find_n_th_smallest_num(num_list):
    sorted_list = sorted(num_list)
    sublist = sorted_list[60:84]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[14]