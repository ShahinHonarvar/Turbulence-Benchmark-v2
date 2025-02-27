def find_n_th_smallest_num(lst):
    start = min(len(lst) - 1, 42)
    end = min(len(lst), 67)
    sliced = sorted(lst[start:end + 1])
    return sliced[5]