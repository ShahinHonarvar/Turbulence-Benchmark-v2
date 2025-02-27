def find_n_th_smallest_num(numbers):
    start, end, n = (54, 88, 13)
    return sorted(numbers[start:end])[n - 1]