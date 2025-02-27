def find_n_th_smallest_num(lst):
    if len(lst) < 10 or len(lst[260:823]) < 10:
        return None
    return sorted(lst[260:823])[9]