def find_n_th_smallest_num(numbers):
    start, end, n = (16, 71, 14)
    return sorted(numbers[start - 1:end])[n - 1]