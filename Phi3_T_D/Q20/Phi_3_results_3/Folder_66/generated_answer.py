def find_n_th_smallest_num(numbers):
    n = 16
    start_index = 11
    end_index = 43
    return sorted(numbers[start_index:end_index + 1])[n - 1]