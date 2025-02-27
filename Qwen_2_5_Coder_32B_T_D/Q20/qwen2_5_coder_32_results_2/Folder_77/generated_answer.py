def find_n_th_smallest_num(lst):
    sublist = lst[106:255]
    sublist.sort()
    return sublist[8]