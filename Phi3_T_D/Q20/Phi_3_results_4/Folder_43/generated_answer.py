def find_n_th_smallest_num(lst):
    start = 28
    end = 64
    sliced_list = lst[start:end + 1]
    sliced_list.sort()
    return sliced_list[15]