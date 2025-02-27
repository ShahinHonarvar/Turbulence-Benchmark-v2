def find_n_th_smallest_num(lst):
    if len(lst) < 5:
        return None
    return sorted(set(lst))[4]