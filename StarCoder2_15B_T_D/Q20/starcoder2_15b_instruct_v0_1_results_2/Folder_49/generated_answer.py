def find_n_th_smallest_num(lst):
    sublist = lst[20:201]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[10]