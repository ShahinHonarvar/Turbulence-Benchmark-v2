def find_n_th_smallest_num(lst):
    if 28 <= len(lst) <= 64:
        return sorted(lst[27:64 + 1])[15]
    return None