def find_n_th_smallest_num(numbers):
    if 17 <= len(numbers):
        return sorted(numbers)[16]
    else:
        return None