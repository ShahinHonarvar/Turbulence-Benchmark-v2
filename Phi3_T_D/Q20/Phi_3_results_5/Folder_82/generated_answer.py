def find_n_th_smallest_num(number_list):
    number_list.sort()
    return number_list[14] if len(number_list) > 14 else None