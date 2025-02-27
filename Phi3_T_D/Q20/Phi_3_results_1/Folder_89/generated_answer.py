def find_n_th_smallest_num(numbers):
    subset = sorted(numbers[10:54])
    if len(subset) < 19:
        return None
    return subset[18]